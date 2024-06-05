%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   genSequence.m   modified on Feb 11, 2023 by CC; created on Jun. 25 2021 by CC
%   generate the stimulus paramters of visual search task (Location Probability Learning)
%
%   Exp Design: 288 trials
%   6 cycles (24 even trials + 24 uneven trials)
%   even trials: 25%  probability  in rich quad, 25% in 3 sparese quads
%   uneven trials: 50%  probability  in rich quad, 16.7% in 3 sparese quads
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Experimental parameters

clear all; clc; sca;

% main exp sequence (1) or prac sequence (99)
%session = 99; totaldesign = 1;
session = 1; totaldesign = 4; % 4 types of design (rich quadrant location)


for whichdesign = 1:totaldesign

    richquad = whichdesign;

    clear datacell;

    %%------------------------------------Experiment Start---------------------------------
    if session~=99
        outputname = ['Seq_Design' num2str(whichdesign) '.xls'];
    else
        outputname = ['Seq_practice.xls'];
        %outputname = ['Seq_keyprac.xls'];
    end

    % %--------------------Block Parameters-----------------

    nblocks = 6; % how many cycles 
    ntrials = 48; % 24 even + 24 uneven trials per cycles

    setsize = 12; % set size
    numPerQuad = setsize./4; % number of items per quadrant

    % %------------------------------------------------------------

    if session==99
        ntrials = 16; % 16 practice trials per block
        firstBlock = 0; finalBlock = 1; % 2 practice blocks (block 0+block 1)
    else
        % main experiment: to make things easier, let's use 24 trials x 12 blocks (1,3,5,7,9,11 block - unbiased/even trials, 2,4,6,8,10,12 block - biased/uneven trials)
        ntrials = ntrials/2; % 24 even + 24 uneven trials per cycles
        firstBlock = 1; finalBlock = nblocks*2;
    end

    if session~=99 && exist(outputname)==2
        fileproblem = input('That file already exists! Append a .x (1), overwrite (2), or break (3/default)?');
        if isempty(fileproblem) || fileproblem==3
            return;
        elseif fileproblem==1
            outputname = [outputname '.x'];
        end
    end

    %     varname = {'phase', 'block', 'trial', 'targOrientdeg', 'targOrient', 'corrAnswer'};

    % phase: even + uneven; block: 6 cycles, trials: 24+24
    varname = {'phase', 'block', 'trial', 'targetQuad', 'Tcondition', ...
        'targOrientdeg', 'targOrient', 'corrAnswer', ...
        'targcell','tlocx', 'tlocy', ...
        'd1x', 'd1y', 'd2x', 'd2y', ...
        'd3x', 'd3y', 'd4x', 'd4y',  ...
        'd5x', 'd5y', 'd6x', 'd6y', ...
        'd7x', 'd7y', 'd8x', 'd8y', ...
        'd9x', 'd9y', 'd10x', 'd10y', ...
        'd11x', 'd11y',...
        'd1Orient', 'd2Orient', 'd3Orient', 'd4Orient', ...
        'd5Orient', 'd6Orient', 'd7Orient', 'd8Orient', ...
        'd9Orient', 'd10Orient', 'd11Orient'};

    % define cell to save xlsx
    [junk columns] = size(varname);
    for coln = 1:columns
        datacell{1,coln} = varname{1,coln};
    end

    % set the item locations. 10x10 matrix, 25 locations per quadrant. The
    % centers of the cell are jittered so that they don't align up perfectly
    nrow = 10; ncolumn = 10;
    cellsize1 = 28+20; % letter size 28 pixels; jitter range -10~+10 pixels
    itemJitterX = [-10:1:10, -10:1:10, -10:1:10, -10:1:10,-10:1:10];
    itemJitterY = itemJitterX;
    itemJitterX = Shuffle(itemJitterX);
    itemJitterY = Shuffle(itemJitterY);
    for ncells = 1:nrow.*ncolumn
        xnum = (mod(ncells-1, ncolumn)+1)-(ncolumn/2)-0.5;
        ynum = (nrow/2)+0.5-ceil(ncells/ncolumn); % different from matlab, coordinate in PsychoPy: positive values mean up/right
        cellcenter(ncells,1) = xnum.*cellsize1 + itemJitterX(ncells);
        cellcenter(ncells,2) = ynum.*cellsize1 + itemJitterY(ncells);
    end

    % remove center 16 cells
    % Lab CRT, 1024*768 resolution, 57cm distance,
    % then 28 pixel/degree, so 6.7 degree fovea in diameter  = 187.6 pixels in diameter, 93.8 pixels in radius
    quad1 = [6 7 8 9 10 16 17 18 19 20 26 27 28 29 30 38 39 40 48 49 50]; %upper right
    quad2 = [1 2 3 4 5 11 12 13 14 15 21 22 23 24 25 31 32 33 41 42 43]; %upper left
    quad3 = [51 52 53 61 62 63 71 72 73 74 75 81 82 83 84 85 91 92 93 94 95]; %lower left
    quad4 = [58 59 60 68 69 70 76 77 78 79 80 86 87 88 89 90 96 97 98 99 100]; %lower right

    %         % all 100 possible locations
    %         quad1 = [6 7 8 9 10 16 17 18 19 20 26 27 28 29 30 36 37 38 39 40 46 47 48 49 50]; %upper right
    %         quad2 = [1 2 3 4 5 11 12 13 14 15 21 22 23 24 25 31 32 33 34 35 41 42 43 44 45]; %upper left
    %         quad3 = [51 52 53 54 55 61 62 63 64 65 71 72 73 74 75 81 82 83 84 85 91 92 93 94 95]; %lower left
    %         quad4 = [56 57 58 59 60 66 67 68 69 70 76 77 78 79 80 86 87 88 89 90 96 97 98 99 100]; %lower right

    matrixloc = [quad1; quad2; quad3; quad4];

    % now figure out where to place the items
    itemloc = zeros(setsize, 4); % the x1,y1,x2,y2 for each of the setsize number of items
    targlocs = zeros(ntrials, 1); % 24 target locations
    distlocs = zeros(ntrials, setsize-1); % for each display, setsize-1 distractors


    % experiemnt design: targloc 12 rich quad, 12 sparese quad
    allquad = [1 2 3 4];
    sparquad = allquad(allquad~=richquad);
    if session~=99
        unevenMatrix = [repmat(richquad,1,ntrials/2),repmat(sparquad(1),1,ntrials/6),repmat(sparquad(2),1,ntrials/6),repmat(sparquad(3),1,ntrials/6)];  % uneven phase: 3:1:1:1 (50%:50%)
        evenMatrix = [repmat(richquad,1,ntrials/4),repmat(sparquad(1),1,ntrials/4),repmat(sparquad(2),1,ntrials/4),repmat(sparquad(3),1,ntrials/4)];  % even phase: 1:1:1:1
    end

    %% ---------------------Block Start---------------------
    rown = 1; % trials number
    for k = firstBlock:finalBlock

        % target quad in block
        if session~=99
            if mod(k,2) == 0 % 2,4,6,8,10,12 block - unbiased/even trials
                targquad = Shuffle(unevenMatrix); % 50%:16.7%: 16.7%: 16.7%
            else % 1,3,5,7,9,11 block - biased/uneven trials
                targquad = Shuffle(evenMatrix);  % 25% 25%:25%:25%
            end
        else
            % practice block
            evenMatrix = repmat([1,2,3,4],1,ntrials/4);
            targquad = Shuffle(evenMatrix);
        end

        % Shuffle target and distractor locations
        for i = 1:ntrials
            newmatrix = [Shuffle(matrixloc(1,:)); Shuffle(matrixloc(2,:)); Shuffle(matrixloc(3,:)); Shuffle(matrixloc(4,:))];

            nontargQuads(i,:) = allquad(allquad~=targquad(i));

            % choose targer loccation from target quadrant
            targlocs(i) = newmatrix(targquad(i),1);

            % choose distractor locations from the three non-target quadrants
            distlocs(i, 1:numPerQuad) = newmatrix(nontargQuads(i,1), 1:numPerQuad);
            distlocs(i, numPerQuad+1:numPerQuad.*2) = newmatrix(nontargQuads(i,2), 1:numPerQuad);
            distlocs(i, numPerQuad.*2+1:numPerQuad.*3) = newmatrix(nontargQuads(i,3), 1:numPerQuad);

            % now choose the distractor locations in the target's quadrant.
            distindex=numPerQuad*3+1; % the following loop is to make sure that distractors don't overlap with the target
            for j = 1:numPerQuad
                if newmatrix(targquad(i),j)~=targlocs(i);
                    distlocs(i,distindex)=newmatrix(targquad(i),j);
                    distindex=(distindex+1);
                end
                if distindex==setsize
                    break;
                end
            end

        end

        % T target orientation
        targorient = Shuffle(1:ntrials);

        %% ---------------------Trial Start---------------------
        if session~=99
            if mod(k,2) == 0 % 2,4,6,8,10,12 block - biased/uneven trials
                phase = 'uneven';
            else % 1,3,5,7,9,11 block - unbiased/even trials
                phase = 'even';
            end
        else
            phase = 'practice';
        end

        for l = 1:ntrials

            if targquad(l)== richquad
                condT='rich';
            else
                condT='sparse';
            end

            % Distractor (Ls) and target (T)
            for m = 1:setsize-1
                distOrientation(m) = ceil(rand*4)*90; % random orientation
                dx(m) = cellcenter(distlocs(l, m),1);
                dy(m) = cellcenter(distlocs(l, m),2);
            end
            tlocx = cellcenter(targlocs(l),1);
            tlocy = cellcenter(targlocs(l),2);
            if mod(targorient(l),2)==1
                targetOrientation = 0;
                targOrientcond = 'left';
                corrAns = 'a';
            else
                targetOrientation = 180;
                targOrientcond = 'right';
                corrAns = 's';
            end

            %             data = {phase, k, l, targetOrientation, targOrientcond, corrAns};

            if session ~= 99 % main experiment
                % save whichblock and whichtrial
                whichblock = round(k/2); % 1,1,2,2,3,3,4,4,5,5,6,6 blocks
                whichtrial = l+24*mod(k+1,2); % 1-48 trials
            end

            data = {phase, whichblock, whichtrial, targquad(l), condT, ...
                targetOrientation, targOrientcond, corrAns,...
                targlocs(l), tlocx, tlocy,  ...
                dx(1), dy(1), dx(2), dy(2), ...
                dx(3), dy(3), dx(4), dy(4), ...
                dx(5), dy(5), dx(6), dy(6), ...
                dx(7), dy(7), dx(8), dy(8), ...
                dx(9), dy(9), dx(10), dy(10),...
                dx(11), dy(11),...
                distOrientation(1), distOrientation(2), distOrientation(3), ...
                distOrientation(4), distOrientation(5), distOrientation(6), ...
                distOrientation(7), distOrientation(8), distOrientation(9), ...
                distOrientation(10), distOrientation(11)};

            % save data in cell format
            rown = rown+1;
            for coln = 1:columns
                datacell{rown,coln} = data{1,coln};
            end

        end % trial loop
    end % block loop

    %fclose(outfile);
    writetable(table(datacell),[outputname,'x'],'Sheet',1,'WriteVariableNames',false); % save xlsx file

    fprintf('\n\n\n\n\nDone generating the file...\n\n');

end %  design loops
