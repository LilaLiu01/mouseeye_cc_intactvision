
clear all; clc; sca;

%% create aperture mask

N=8000;  % mask size (large enough to cover all screen in all mouse location, radius(N/2) should be the max resolution, 4000 pixels)
% in Lab CRT, 1024*768 resolution, 57cm distance, then 28 pixel/degree
% so 6.7 degree fovea in diameter  = 187.60 pixels in diameter, 93.8 pixels in radius
R=93.8;   % center aperture size

%  background
D=255*ones(N,N);

% filter indise circle
i0=N/2; j0=N/2;
[x,y]=meshgrid(1:N);
D((x-i0).^2+(y-j0).^2<R^2)=0;

imdata = uint8(cat(3, D, D, D));
%imwrite(imdata,'circleMask.png');


%% add guassian low-pass filter

%orgImage = imread('circleMask.jpg');
orgImage = imdata;

sigma = 28/2; % guassian filter standard deviation (0.5 degree)

% % method 1: fspecial, using "fspecial" is not recommended for 2-D Gaussian filtering of images
% kernel = fspecial('gaussian', [sigma*3*2 sigma*3*2], sigma); % size of Gaussian blur operator with standard deviation
% surf(kernel); % show kernel
% blurredImage = imfilter(orgImage, kernel);
% figure; imshow(blurredImage);

% method 2: imgaussfilt, optionally the sigma value and size of the Gaussian filter
blurredImage = imgaussfilt(orgImage, sigma); % Gaussian filter standard deviation
figure; imshow(blurredImage);

imwrite(blurredImage,'circleMask.png');


%% create background image

%  background
D=128*ones(N,N);

imdata = uint8(cat(3, D, D, D));
imwrite(imdata,'plainBackground.png')



%% create fixation

N=280;  % mask size (28 pixel in psychopy)
R=280*0.75/2;  % center aperture size (0.75 degree in diameter = 28/2 *0.75 pixels)

%  background
D=128*ones(N,N);

% filter indise circle
i0=N/2; j0=N/2;
[x,y]=meshgrid(1:N);
D((x-i0).^2+(y-j0).^2<R^2)=255;

imdata = uint8(cat(3, D, D, D));
imwrite(imdata,'fixation.png');


%% create green fixation

N=280;  % mask size (28 pixel in psychopy)
R=280*0.75/2;  % center aperture size (0.75 degree in diameter = 28/2 *0.75 pixels)

%  background
D1=128*ones(N,N);
D2=128*ones(N,N);
D3=128*ones(N,N);

% filter indise circle
i0=N/2; j0=N/2;
[x,y]=meshgrid(1:N);
D1((x-i0).^2+(y-j0).^2<R^2)=0; %R
D2((x-i0).^2+(y-j0).^2<R^2)=255; %G
D3((x-i0).^2+(y-j0).^2<R^2)=0; %B

imdata = uint8(cat(3, D1, D2, D3));
imwrite(imdata,'greenfixation.png');
