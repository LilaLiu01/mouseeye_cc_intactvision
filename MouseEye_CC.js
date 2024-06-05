/******************** 
 * Mouseeye_Cc *
 ********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'MouseEye_CC';  // from the Builder filename that created this script
let expInfo = {
    'participant': '999',
    'designid': '12',
    'prolificid': 'xxx',
    'Gender': 'F',
    'Age': '18',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'pix',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstrStartPageRoutineBegin());
flowScheduler.add(InstrStartPageRoutineEachFrame());
flowScheduler.add(InstrStartPageRoutineEnd());
flowScheduler.add(VirtualChinrestRoutineBegin());
flowScheduler.add(VirtualChinrestRoutineEachFrame());
flowScheduler.add(VirtualChinrestRoutineEnd());
flowScheduler.add(InstrRedoRoutineBegin());
flowScheduler.add(InstrRedoRoutineEachFrame());
flowScheduler.add(InstrRedoRoutineEnd());
flowScheduler.add(VirtualChinrest_RedoRoutineBegin());
flowScheduler.add(VirtualChinrest_RedoRoutineEachFrame());
flowScheduler.add(VirtualChinrest_RedoRoutineEnd());
flowScheduler.add(Instruction1RoutineBegin());
flowScheduler.add(Instruction1RoutineEachFrame());
flowScheduler.add(Instruction1RoutineEnd());
const keyPracLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(keyPracLoopLoopBegin(keyPracLoopLoopScheduler));
flowScheduler.add(keyPracLoopLoopScheduler);
flowScheduler.add(keyPracLoopLoopEnd);



flowScheduler.add(Instruction2RoutineBegin());
flowScheduler.add(Instruction2RoutineEachFrame());
flowScheduler.add(Instruction2RoutineEnd());
flowScheduler.add(Instruction3RoutineBegin());
flowScheduler.add(Instruction3RoutineEachFrame());
flowScheduler.add(Instruction3RoutineEnd());
const trialsPracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeLoopBegin(trialsPracticeLoopScheduler));
flowScheduler.add(trialsPracticeLoopScheduler);
flowScheduler.add(trialsPracticeLoopEnd);





flowScheduler.add(CheckInstrRoutineBegin());
flowScheduler.add(CheckInstrRoutineEachFrame());
flowScheduler.add(CheckInstrRoutineEnd());
flowScheduler.add(CheckInstr_FBRoutineBegin());
flowScheduler.add(CheckInstr_FBRoutineEachFrame());
flowScheduler.add(CheckInstr_FBRoutineEnd());
flowScheduler.add(Instruction_MainExpRoutineBegin());
flowScheduler.add(Instruction_MainExpRoutineEachFrame());
flowScheduler.add(Instruction_MainExpRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);






const TestingtrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(TestingtrialsLoopBegin(TestingtrialsLoopScheduler));
flowScheduler.add(TestingtrialsLoopScheduler);
flowScheduler.add(TestingtrialsLoopEnd);






flowScheduler.add(RecogQuestionRoutineBegin());
flowScheduler.add(RecogQuestionRoutineEachFrame());
flowScheduler.add(RecogQuestionRoutineEnd());
flowScheduler.add(DiscloseRoutineBegin());
flowScheduler.add(DiscloseRoutineEachFrame());
flowScheduler.add(DiscloseRoutineEnd());
flowScheduler.add(InstrRTRoutineBegin());
flowScheduler.add(InstrRTRoutineEachFrame());
flowScheduler.add(InstrRTRoutineEnd());
const RTtrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RTtrialsLoopBegin(RTtrialsLoopScheduler));
flowScheduler.add(RTtrialsLoopScheduler);
flowScheduler.add(RTtrialsLoopEnd);



flowScheduler.add(EndOfExperimentRoutineBegin());
flowScheduler.add(EndOfExperimentRoutineEachFrame());
flowScheduler.add(EndOfExperimentRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Seq_keyprac.xlsx', 'path': 'Seq_keyprac.xlsx'},
    {'name': 'Seq_practice.xlsx', 'path': 'Seq_practice.xlsx'},
    {'name': 'instr1_key.png', 'path': 'instr1_key.png'},
    {'name': 'T.png', 'path': 'T.png'},
    {'name': 'instr2_search.png', 'path': 'instr2_search.png'},
    {'name': 'instr3_fix.png', 'path': 'instr3_fix.png'},
    {'name': 'fixation.png', 'path': 'fixation.png'},
    {'name': 'greenfixation.png', 'path': 'greenfixation.png'},
    {'name': 'L.png', 'path': 'L.png'},
    {'name': 'plainBackground.png', 'path': 'plainBackground.png'},
    {'name': 'circleMask.png', 'path': 'circleMask.png'},
    {'name': 'Testing_Seq1.xlsx', 'path': 'Testing_Seq1.xlsx'},
    {'name': 'Testing_Seq2.xlsx', 'path': 'Testing_Seq2.xlsx'},
    {'name': 'Testing_Seq3.xlsx', 'path': 'Testing_Seq3.xlsx'},
    {'name': 'Testing_Seq4.xlsx', 'path': 'Testing_Seq4.xlsx'},
    {'name': 'Testing_Seq5.xlsx', 'path': 'Testing_Seq5.xlsx'},
    {'name': 'Testing_Seq6.xlsx', 'path': 'Testing_Seq6.xlsx'},
    {'name': 'Testing_Seq7.xlsx', 'path': 'Testing_Seq7.xlsx'},
    {'name': 'Testing_Seq8.xlsx', 'path': 'Testing_Seq8.xlsx'},
    {'name': 'Testing_Seq9.xlsx', 'path': 'Testing_Seq9.xlsx'},
    {'name': 'Testing_Seq10.xlsx', 'path': 'Testing_Seq10.xlsx'},
    {'name': 'Testing_Seq11.xlsx', 'path': 'Testing_Seq11.xlsx'},
    {'name': 'Testing_Seq12.xlsx', 'path': 'Testing_Seq12.xlsx'},
    {'name': 'MouseEyeCC_Seq1.xlsx', 'path': 'MouseEyeCC_Seq1.xlsx'},
    {'name': 'MouseEyeCC_Seq2.xlsx', 'path': 'MouseEyeCC_Seq2.xlsx'},
    {'name': 'MouseEyeCC_Seq3.xlsx', 'path': 'MouseEyeCC_Seq3.xlsx'},
    {'name': 'MouseEyeCC_Seq4.xlsx', 'path': 'MouseEyeCC_Seq4.xlsx'},
    {'name': 'MouseEyeCC_Seq5.xlsx', 'path': 'MouseEyeCC_Seq5.xlsx'},
    {'name': 'MouseEyeCC_Seq6.xlsx', 'path': 'MouseEyeCC_Seq6.xlsx'},
    {'name': 'MouseEyeCC_Seq7.xlsx', 'path': 'MouseEyeCC_Seq7.xlsx'},
    {'name': 'MouseEyeCC_Seq8.xlsx', 'path': 'MouseEyeCC_Seq8.xlsx'},
    {'name': 'MouseEyeCC_Seq9.xlsx', 'path': 'MouseEyeCC_Seq9.xlsx'},
    {'name': 'MouseEyeCC_Seq10.xlsx', 'path': 'MouseEyeCC_Seq10.xlsx'},
    {'name': 'MouseEyeCC_Seq11.xlsx', 'path': 'MouseEyeCC_Seq11.xlsx'},
    {'name': 'MouseEyeCC_Seq12.xlsx', 'path': 'MouseEyeCC_Seq12.xlsx'},
    {'name': 'RT_Seq1.xlsx', 'path': 'RT_Seq1.xlsx'},
    {'name': 'RT_Seq2.xlsx', 'path': 'RT_Seq2.xlsx'},
    {'name': 'RT_Seq3.xlsx', 'path': 'RT_Seq3.xlsx'},
    {'name': 'RT_Seq4.xlsx', 'path': 'RT_Seq4.xlsx'},
    {'name': 'RT_Seq5.xlsx', 'path': 'RT_Seq5.xlsx'},
    {'name': 'RT_Seq6.xlsx', 'path': 'RT_Seq6.xlsx'},
    {'name': 'RT_Seq7.xlsx', 'path': 'RT_Seq7.xlsx'},
    {'name': 'RT_Seq8.xlsx', 'path': 'RT_Seq8.xlsx'},
    {'name': 'RT_Seq9.xlsx', 'path': 'RT_Seq9.xlsx'},
    {'name': 'RT_Seq10.xlsx', 'path': 'RT_Seq10.xlsx'},
    {'name': 'RT_Seq11.xlsx', 'path': 'RT_Seq11.xlsx'},
    {'name': 'RT_Seq12.xlsx', 'path': 'RT_Seq12.xlsx'},
    {'name': 'greenfixation.png', 'path': 'greenfixation.png'},
    {'name': 'styles.css', 'path': 'styles.css'},
    {'name': 'card.png', 'path': 'card.png'},
    {'name': 'circleMask.png', 'path': 'circleMask.png'},
    {'name': 'fixation.png', 'path': 'fixation.png'},
    {'name': 'instr1_key.png', 'path': 'instr1_key.png'},
    {'name': 'instr2_search.png', 'path': 'instr2_search.png'},
    {'name': 'instr3_fix.png', 'path': 'instr3_fix.png'},
    {'name': 'instr4_hidden.png', 'path': 'instr4_hidden.png'},
    {'name': 'instr5_fixagain.png', 'path': 'instr5_fixagain.png'},
    {'name': 'L.png', 'path': 'L.png'},
    {'name': 'plainBackground.png', 'path': 'plainBackground.png'},
    {'name': 'T.png', 'path': 'T.png'},
    {'name': 'Seq_keyprac.xlsx', 'path': 'Seq_keyprac.xlsx'},
    {'name': 'Seq_practice.xlsx', 'path': 'Seq_practice.xlsx'},
    {'name': 'virtual_chinrest.html', 'path': 'virtual_chinrest.html'},
    {'name': 'virtual_chinrest.js', 'path': 'virtual_chinrest.js'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.com/submissions/complete?cc=C1O4UQYA', 'https://umn.qualtrics.com/jfe/form/SV_eX2X12WKLn0nWu2');


  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var InstrStartPageClock;
var design;
var parameterfile;
var testingfile;
var rtfile;
var InstrStartPage_text;
var InstrStartPage_key;
var VirtualChinrestClock;
var loading;
var InstrRedoClock;
var InstrRedo_txt;
var InstrRedo_key;
var VirtualChinrest_RedoClock;
var loading_redo;
var Instruction1Clock;
var instr1_key;
var key_instr1key;
var keyPracticeClock;
var hintlocation;
var fixation_keyprac;
var letterT;
var keyHint;
var key_keyprac;
var keyPracFeedbackClock;
var keyFeedback;
var sumaccKeyPrac;
var Instruction2Clock;
var instr2_search;
var key_instr2search;
var Instruction3Clock;
var instr3_fix;
var key_instr3fix;
var fixationClock;
var fixsize;
var fixationPoint;
var fixationHint;
var mouseintial;
var greenFixationClock;
var fixationPoint_2;
var trialClock;
var lettersize;
var aperturesize;
var searchsize;
var newtlocx;
var newtlocy;
var newd1x;
var newd1y;
var newd2x;
var newd2y;
var newd3x;
var newd3y;
var newd4x;
var newd4y;
var newd5x;
var newd5y;
var newd6x;
var newd6y;
var newd7x;
var newd7y;
var newd8x;
var newd8y;
var newd9x;
var newd9y;
var newd10x;
var newd10y;
var newd11x;
var newd11y;
var background;
var imageT;
var imageL1;
var imageL2;
var imageL3;
var imageL4;
var imageL5;
var imageL6;
var imageL7;
var imageL8;
var imageL9;
var imageL10;
var imageL11;
var imageAperture;
var CenterAperture;
var searchHint;
var key_respMain;
var trialFeedbackClock;
var textFeedback;
var CheckInstrClock;
var text_checkInstr;
var checkIntr_example;
var key_checkInstr;
var CheckInstr_FBClock;
var feedback_CheckInstr1;
var feedback_CheckInstr2;
var key_feedbackCheckInstr;
var Instruction_MainExpClock;
var InstrMainExp;
var key_InstrMainExp;
var TakeABreakClock;
var sumcorr;
var avgcorr;
var sumrt;
var avgrt;
var accfbcolor;
var rtfbcolor;
var accfbtext;
var rtfbtext;
var acctext;
var rttext;
var textBreak;
var textBlockRemaining;
var key_respBreak;
var displayTestingPhaseClock;
var background_3;
var imageT_3;
var imageL1_3;
var imageL2_3;
var imageL3_3;
var imageL4_3;
var imageL5_3;
var imageL6_3;
var imageL7_3;
var imageL8_3;
var imageL9_3;
var imageL10_3;
var imageL11_3;
var imageAperture_3;
var CenterAperture_3;
var key_respTesting;
var TakeABreak2Clock;
var accText;
var rtText;
var TextBreak;
var textblockRemaining;
var key_RespBreak;
var RecogQuestionClock;
var Ques_text;
var key_AnswerQues;
var DiscloseClock;
var Disclose_text;
var continue_key;
var InstrRTClock;
var InstrRecognitionTest;
var InstrRecognitionTest_key;
var fixation_RTClock;
var fixation_image;
var fixationHint_text;
var mouseInitial;
var displayRTClock;
var background_2;
var imageT_2;
var imageL1_2;
var imageL2_2;
var imageL3_2;
var imageL4_2;
var imageL5_2;
var imageL6_2;
var imageL7_2;
var imageL8_2;
var imageL9_2;
var imageL10_2;
var imageL11_2;
var imageAperture_2;
var CenterAperture_2;
var key_respRT;
var adjustHint_text;
var EndOfExperimentClock;
var textEnd;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "InstrStartPage"
  InstrStartPageClock = new util.Clock();
  // Run 'Begin Experiment' code from StartPage_code
  if (((Number.parseInt(expInfo["Age"]) < 18) || (Number.parseInt(expInfo["Age"]) > 45))) {
      core.quit();
  }
  design = Number.parseInt(expInfo["designid"]);
  parameterfile = (("MouseEyeCC_Seq" + design.toString()) + ".xlsx");
  testingfile = (("Testing_Seq" + design.toString()) + ".xlsx");
  rtfile = (("RT_Seq" + design.toString()) + ".xlsx");
  expInfo["ratio_monitor2CRT"] = 1;
  
  InstrStartPage_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrStartPage_text',
    text: 'Welcome to our study! \n\nThis study requires about 20 minutes of uninterrupted time. Please choose a comfortable pose and try to keep the same pose during experiment. \n\nWe will first find out your monitor size, how far away you are sitting. Then you will do a visual search task.\n\nPress the spacebar to start when you are ready.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -1.0 
  });
  
  InstrStartPage_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "VirtualChinrest"
  VirtualChinrestClock = new util.Clock();
  loading = new visual.TextStim({
    win: psychoJS.window,
    name: 'loading',
    text: 'Loading......',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "InstrRedo"
  InstrRedoClock = new util.Clock();
  InstrRedo_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrRedo_txt',
    text: 'You might sit too far away. Please sit closer to your screen.\n\nWe will find out your current distance. When you are ready, press spacebar to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 28.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -2.0 
  });
  
  InstrRedo_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "VirtualChinrest_Redo"
  VirtualChinrest_RedoClock = new util.Clock();
  loading_redo = new visual.TextStim({
    win: psychoJS.window,
    name: 'loading_redo',
    text: 'Please wait a second. Loading......',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Instruction1"
  Instruction1Clock = new util.Clock();
  instr1_key = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instr1_key', units : undefined, 
    image : 'instr1_key.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [641, 488],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : 0.0 
  });
  key_instr1key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "keyPractice"
  keyPracticeClock = new util.Clock();
  // Run 'Begin Experiment' code from code_keyprac
  hintlocation = 255;
  
  fixation_keyprac = new visual.Polygon({
    win: psychoJS.window, name: 'fixation_keyprac', 
    edges: 100, size:[20, 20],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  letterT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'letterT', units : undefined, 
    image : 'T.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : [80, 80],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -2.0 
  });
  keyHint = new visual.TextStim({
    win: psychoJS.window,
    name: 'keyHint',
    text: 'A key (tip of T facing left), S key (facing right)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  key_keyprac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "keyPracFeedback"
  keyPracFeedbackClock = new util.Clock();
  keyFeedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'keyFeedback',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 32,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from code_endkeyprac
  sumaccKeyPrac = 0;
  
  // Initialize components for Routine "Instruction2"
  Instruction2Clock = new util.Clock();
  instr2_search = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instr2_search', units : undefined, 
    image : 'instr2_search.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [594, 465],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : 0.0 
  });
  key_instr2search = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruction3"
  Instruction3Clock = new util.Clock();
  instr3_fix = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instr3_fix', units : undefined, 
    image : 'instr3_fix.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [501, 234],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : 0.0 
  });
  key_instr3fix = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  // Run 'Begin Experiment' code from code_fixinitial
  fixsize = 28;
  hintlocation = 255;
  
  fixationPoint = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixationPoint', units : undefined, 
    image : 'fixation.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  fixationHint = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationHint',
    text: 'please click the white dot in the center to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  mouseintial = new core.Mouse({
    win: psychoJS.window,
  });
  mouseintial.mouseClock = new util.Clock();
  // Initialize components for Routine "greenFixation"
  greenFixationClock = new util.Clock();
  // Run 'Begin Experiment' code from code_fixinitial_2
  fixsize = 28;
  hintlocation = 255;
  
  fixationPoint_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixationPoint_2', units : undefined, 
    image : 'greenfixation.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  // Run 'Begin Experiment' code from code_initial
  lettersize = 28;
  aperturesize = 8000;
  searchsize = 482;
  newtlocx = 0;
  newtlocy = 0;
  newd1x = 0;
  newd1y = 0;
  newd2x = 0;
  newd2y = 0;
  newd3x = 0;
  newd3y = 0;
  newd4x = 0;
  newd4y = 0;
  newd5x = 0;
  newd5y = 0;
  newd6x = 0;
  newd6y = 0;
  newd7x = 0;
  newd7y = 0;
  newd8x = 0;
  newd8y = 0;
  newd9x = 0;
  newd9y = 0;
  newd10x = 0;
  newd10y = 0;
  newd11x = 0;
  newd11y = 0;
  hintlocation = 255;
  
  background = new visual.Rect ({
    win: psychoJS.window, name: 'background', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('gray'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  imageT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT', units : undefined, 
    image : 'T.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -2.0 
  });
  imageL1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL1', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -3.0 
  });
  imageL2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -4.0 
  });
  imageL3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -5.0 
  });
  imageL4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL4', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -6.0 
  });
  imageL5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL5', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -7.0 
  });
  imageL6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL6', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -8.0 
  });
  imageL7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL7', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -9.0 
  });
  imageL8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL8', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -10.0 
  });
  imageL9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL9', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -11.0 
  });
  imageL10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL10', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -12.0 
  });
  imageL11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL11', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -13.0 
  });
  imageAperture = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageAperture', units : undefined, 
    image : 'plainBackground.png', mask : 'circleMask.png',
    anchor : 'center',
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -14.0 
  });
  CenterAperture = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CenterAperture', units : undefined, 
    image : 'plainBackground.png', mask : 'circleMask.png',
    anchor : 'center',
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -15.0 
  });
  searchHint = new visual.TextStim({
    win: psychoJS.window,
    name: 'searchHint',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -16.0 
  });
  
  key_respMain = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trialFeedback"
  trialFeedbackClock = new util.Clock();
  textFeedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'textFeedback',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 32,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "CheckInstr"
  CheckInstrClock = new util.Clock();
  text_checkInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_checkInstr',
    text: 'End of practice. To make sure you understand the instructions, we have a question for you.\n\nNow suppose the tip of letter T points toward left, like this:\n\n\n\n\n\n\n\nWhich button will your press?\n\nPress A or S key to respond.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  checkIntr_example = new visual.ImageStim({
    win : psychoJS.window,
    name : 'checkIntr_example', units : undefined, 
    image : 'T.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [60, 60],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : -1.0 
  });
  key_checkInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "CheckInstr_FB"
  CheckInstr_FBClock = new util.Clock();
  feedback_CheckInstr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_CheckInstr1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  feedback_CheckInstr2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_CheckInstr2',
    text: 'Please press spacebar to continue.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 70)], height: 24,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_feedbackCheckInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruction_MainExp"
  Instruction_MainExpClock = new util.Clock();
  InstrMainExp = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrMainExp',
    text: 'Now we begin the real experiment!\n\nThe task is the same as the practice you just did: click the white dot to start, then move your mouse around to find letter T. This experiment takes about 15 minutes. There are 24 blocks. At the end of each block, you will see your response accuracy and can take a short break. \n\nPlease respond as accurately and quickly as possible, and try to keep the same pose during experiment.\n\nReady? Press spacebar to start!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_InstrMainExp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TakeABreak"
  TakeABreakClock = new util.Clock();
  // Run 'Begin Experiment' code from code_break
  sumcorr = 0;
  avgcorr = 0;
  sumrt = 0;
  avgrt = 0;
  accfbcolor = "white";
  rtfbcolor = "white";
  accfbtext = "na";
  rtfbtext = "na";
  
  acctext = new visual.TextStim({
    win: psychoJS.window,
    name: 'acctext',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 120], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -1.0 
  });
  
  rttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'rttext',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 60], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -2.0 
  });
  
  textBreak = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBreak',
    text: 'There are 24 blocks altogether. The number of remaining blocks is:\n\n\nPress spacebar to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 50)], height: 24,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  textBlockRemaining = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlockRemaining',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  key_respBreak = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "displayTestingPhase"
  displayTestingPhaseClock = new util.Clock();
  // Run 'Begin Experiment' code from code_initial_3
  lettersize = 28;
  aperturesize = 8000;
  searchsize = 482;
  newtlocx = 0;
  newtlocy = 0;
  newd1x = 0;
  newd1y = 0;
  newd2x = 0;
  newd2y = 0;
  newd3x = 0;
  newd3y = 0;
  newd4x = 0;
  newd4y = 0;
  newd5x = 0;
  newd5y = 0;
  newd6x = 0;
  newd6y = 0;
  newd7x = 0;
  newd7y = 0;
  newd8x = 0;
  newd8y = 0;
  newd9x = 0;
  newd9y = 0;
  newd10x = 0;
  newd10y = 0;
  newd11x = 0;
  newd11y = 0;
  hintlocation = 255;
  
  background_3 = new visual.Rect ({
    win: psychoJS.window, name: 'background_3', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('gray'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  imageT_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT_3', units : undefined, 
    image : 'T.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -2.0 
  });
  imageL1_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL1_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -3.0 
  });
  imageL2_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL2_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -4.0 
  });
  imageL3_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL3_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -5.0 
  });
  imageL4_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL4_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -6.0 
  });
  imageL5_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL5_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -7.0 
  });
  imageL6_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL6_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -8.0 
  });
  imageL7_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL7_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -9.0 
  });
  imageL8_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL8_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -10.0 
  });
  imageL9_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL9_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -11.0 
  });
  imageL10_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL10_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -12.0 
  });
  imageL11_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL11_3', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -13.0 
  });
  imageAperture_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageAperture_3', units : undefined, 
    image : 'plainBackground.png', mask : 'circleMask.png',
    anchor : 'center',
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -14.0 
  });
  CenterAperture_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CenterAperture_3', units : undefined, 
    image : 'plainBackground.png', mask : 'circleMask.png',
    anchor : 'center',
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -15.0 
  });
  key_respTesting = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TakeABreak2"
  TakeABreak2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_break2
  sumcorr = 0;
  avgcorr = 0;
  sumrt = 0;
  avgrt = 0;
  accfbcolor = "white";
  rtfbcolor = "white";
  accfbtext = "na";
  rtfbtext = "na";
  
  accText = new visual.TextStim({
    win: psychoJS.window,
    name: 'accText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 120], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(accfbcolor),  opacity: 1.0,
    depth: -1.0 
  });
  
  rtText = new visual.TextStim({
    win: psychoJS.window,
    name: 'rtText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 60], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(rtfbcolor),  opacity: 1.0,
    depth: -2.0 
  });
  
  TextBreak = new visual.TextStim({
    win: psychoJS.window,
    name: 'TextBreak',
    text: 'There are 24 blocks altogether. The number of remaining blocks is:\n\n\nPress spacebar to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 50)], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -3.0 
  });
  
  textblockRemaining = new visual.TextStim({
    win: psychoJS.window,
    name: 'textblockRemaining',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -4.0 
  });
  
  key_RespBreak = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "RecogQuestion"
  RecogQuestionClock = new util.Clock();
  Ques_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Ques_text',
    text: 'Thank you for completing the experiment! Here is a question for you.\n\nDuring the experiment, did you notice that some displays are repeatedly presented across blocks? \n\nPlease press Y for yes, N for no if you did not notice any repeated displays.\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: undefined,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_AnswerQues = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Disclose"
  DiscloseClock = new util.Clock();
  Disclose_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Disclose_text',
    text: 'Thank you for your answer.\n\nIn fact, some displays are repeatedly presented across blocks in the experiment!\n\nPress spacebar to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "InstrRT"
  InstrRTClock = new util.Clock();
  InstrRecognitionTest = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrRecognitionTest',
    text: 'At the end, your task is to indicate whether you have seen the following displays during the course of the experiment or not. \n\nPlease respond as accurately as possible by using the Y key (Yes I have) and N key (No I have not).\n\nReady? Press spacebar to start!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: 0.0 
  });
  
  InstrRecognitionTest_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation_RT"
  fixation_RTClock = new util.Clock();
  // Run 'Begin Experiment' code from code_RTfix
  fixsize = 28;
  hintlocation = 255;
  
  fixation_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixation_image', units : undefined, 
    image : 'fixation.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  fixationHint_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationHint_text',
    text: 'please click the white dot in the center to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  mouseInitial = new core.Mouse({
    win: psychoJS.window,
  });
  mouseInitial.mouseClock = new util.Clock();
  // Initialize components for Routine "displayRT"
  displayRTClock = new util.Clock();
  // Run 'Begin Experiment' code from code_initial_2
  lettersize = 28;
  aperturesize = 8000;
  searchsize = 482;
  newtlocx = 0;
  newtlocy = 0;
  newd1x = 0;
  newd1y = 0;
  newd2x = 0;
  newd2y = 0;
  newd3x = 0;
  newd3y = 0;
  newd4x = 0;
  newd4y = 0;
  newd5x = 0;
  newd5y = 0;
  newd6x = 0;
  newd6y = 0;
  newd7x = 0;
  newd7y = 0;
  newd8x = 0;
  newd8y = 0;
  newd9x = 0;
  newd9y = 0;
  newd10x = 0;
  newd10y = 0;
  newd11x = 0;
  newd11y = 0;
  hintlocation = 255;
  
  background_2 = new visual.Rect ({
    win: psychoJS.window, name: 'background_2', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('gray'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  imageT_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT_2', units : undefined, 
    image : 'T.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -2.0 
  });
  imageL1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL1_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -3.0 
  });
  imageL2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL2_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -4.0 
  });
  imageL3_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL3_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -5.0 
  });
  imageL4_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL4_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -6.0 
  });
  imageL5_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL5_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -7.0 
  });
  imageL6_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL6_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -8.0 
  });
  imageL7_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL7_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -9.0 
  });
  imageL8_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL8_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -10.0 
  });
  imageL9_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL9_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -11.0 
  });
  imageL10_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL10_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -12.0 
  });
  imageL11_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageL11_2', units : undefined, 
    image : 'L.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -13.0 
  });
  imageAperture_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageAperture_2', units : undefined, 
    image : 'plainBackground.png', mask : 'circleMask.png',
    anchor : 'center',
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -14.0 
  });
  CenterAperture_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CenterAperture_2', units : undefined, 
    image : 'plainBackground.png', mask : 'circleMask.png',
    anchor : 'center',
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -15.0 
  });
  key_respRT = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  adjustHint_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'adjustHint_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -17.0 
  });
  
  // Initialize components for Routine "EndOfExperiment"
  EndOfExperimentClock = new util.Clock();
  textEnd = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEnd',
    text: 'You are all done! Thank you very much for doing the experiment!\n\nTo obtain payment, please wait until you can click [OK] button to get the Prolific Completion Code.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 24,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _InstrStartPage_key_allKeys;
var InstrStartPageComponents;
function InstrStartPageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'InstrStartPage' ---
    t = 0;
    InstrStartPageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('InstrStartPage.started', globalClock.getTime());
    InstrStartPage_key.keys = undefined;
    InstrStartPage_key.rt = undefined;
    _InstrStartPage_key_allKeys = [];
    // keep track of which components have finished
    InstrStartPageComponents = [];
    InstrStartPageComponents.push(InstrStartPage_text);
    InstrStartPageComponents.push(InstrStartPage_key);
    
    for (const thisComponent of InstrStartPageComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstrStartPageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstrStartPage' ---
    // get current time
    t = InstrStartPageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *InstrStartPage_text* updates
    if (t >= 0.0 && InstrStartPage_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrStartPage_text.tStart = t;  // (not accounting for frame time here)
      InstrStartPage_text.frameNStart = frameN;  // exact frame index
      
      InstrStartPage_text.setAutoDraw(true);
    }
    
    
    // *InstrStartPage_key* updates
    if (t >= 0.0 && InstrStartPage_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrStartPage_key.tStart = t;  // (not accounting for frame time here)
      InstrStartPage_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { InstrStartPage_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { InstrStartPage_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { InstrStartPage_key.clearEvents(); });
    }
    
    if (InstrStartPage_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = InstrStartPage_key.getKeys({keyList: ['space'], waitRelease: false});
      _InstrStartPage_key_allKeys = _InstrStartPage_key_allKeys.concat(theseKeys);
      if (_InstrStartPage_key_allKeys.length > 0) {
        InstrStartPage_key.keys = _InstrStartPage_key_allKeys[_InstrStartPage_key_allKeys.length - 1].name;  // just the last key pressed
        InstrStartPage_key.rt = _InstrStartPage_key_allKeys[_InstrStartPage_key_allKeys.length - 1].rt;
        InstrStartPage_key.duration = _InstrStartPage_key_allKeys[_InstrStartPage_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstrStartPageComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstrStartPageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstrStartPage' ---
    for (const thisComponent of InstrStartPageComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('InstrStartPage.stopped', globalClock.getTime());
    InstrStartPage_key.stop();
    // the Routine "InstrStartPage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var continue_routine;
var VirtualChinrestComponents;
function VirtualChinrestRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'VirtualChinrest' ---
    t = 0;
    VirtualChinrestClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('VirtualChinrest.started', globalClock.getTime());
    // Run 'Begin Routine' code from skip_offline
    continueRoutine = false;
    
    // This routine should not start straight away or the screen width and height
    // may be incorrect.
    
    expInfo['xRes'] = screen.width;
    expInfo['yRes'] = screen.height;
    
    //let src = ('demographics.html?xRes='+expInfo['xRes']+'&yRes='+expInfo['yRes']);
    let src = ('virtual_chinrest.html');
    
    continue_routine = true; // Routines can't be ended from within Begin Routine
    $(document).ready(function() {
        // Add custom contents from html file using an iframe:
        $('body').append('<div id="iframe-o" style="visibility: hidden; position: relative; display: table; margin: auto; overflow-x: hidden; overflow-y: scroll !important; -webkit-overflow-y-scrolling:touch !important;"><div id="iframe-m" style="display: table-cell; vertical-align: middle;"><div id="iframe-i" style="display: inline-block; width:100%; overflow-y: hidden; overflow-x: hidden;"><iframe id="iframe" src="'+src+'" frameborder="0" style="width: 100%; overflow-y: hidden; overflow-x: hidden; "></iframe></div></div></div>');
        $('#iframe').on('load',function(iframe){
            // Auto-adjust iframe size:
            $(this).contents().find('html').css({ 'display': 'table', 'width': '100%', 'overflow-x': 'hidden' });
            $('#iframe-o').height($(window).height()-20, true);
            $('#iframe-m').width($(this).contents().find('html').width()+100);
            $('#iframe-i').height ( Math.max ( $(this).contents().find('html').height()+20, $(window).height()-20 ), true );
            $(this).height($(this).contents().find('html').height());
            $('#iframe-o').css('visibility','visible');
            
            //if click submit button in a form:
            $(this).contents().find('form').on('submit',function(e){
                e.preventDefault();
                
                //expose the iframe to the window
                var iframe = $('#iframe');
                window.iframe = iframe; 
                // save viewing distance in cm, pixel density (how many pixels per mm, px2mm)
                // save Ball Position (px), Square Position (px)
                expInfo['viewingdistance_cm'] = iframe[0].contentWindow.document.getElementById("info-h").innerText;
                expInfo['pixeldensity_px2mm'] = iframe[0].contentWindow.document.getElementById("info-lpd").innerText;
                expInfo['BallPos'] = iframe[0].contentWindow.document.getElementById("info-BallPos").innerText;
                expInfo['squarePos'] = iframe[0].contentWindow.document.getElementById("info-squarePos").innerText;
                
                // Remove iframe and continue to next routine when done:
                $('#iframe-o').remove();
                continue_routine = false;
            });
            
        });
    });
    //$('#iframe').attr( 'src', function(i,val){ return val;} );
    // keep track of which components have finished
    VirtualChinrestComponents = [];
    VirtualChinrestComponents.push(loading);
    
    for (const thisComponent of VirtualChinrestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function VirtualChinrestRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'VirtualChinrest' ---
    // get current time
    t = VirtualChinrestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *loading* updates
    if (t >= 0.0 && loading.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loading.tStart = t;  // (not accounting for frame time here)
      loading.frameNStart = frameN;  // exact frame index
      
      loading.setAutoDraw(true);
    }
    
    // continue until button pressed
    continueRoutine = continue_routine;
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of VirtualChinrestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VirtualChinrestRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'VirtualChinrest' ---
    for (const thisComponent of VirtualChinrestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('VirtualChinrest.stopped', globalClock.getTime());
    // Using virtual Chinrest Results (viewing distance, pixel density) to estimate pixel per degree:
    // how many mm per degree
    expInfo['mm2degree'] = Math.tan(Math.PI/180) * (Number.parseFloat(expInfo['viewingdistance_cm']) * 10);
    // how many pixel per degree
    expInfo['px2degree'] = Number.parseFloat(expInfo['pixeldensity_px2mm']) * Number.parseFloat(expInfo['mm2degree']);
    
    // if testing in Lab CRT with 36.6 cm height, 1024x768 resolution, and 57cm viewing distance: 
    // then 2.79 pixel per mm, 27.83 pixel per degree
    // CRT_pixeldensity_px2mm = 1024/366;
    // CRT_mm2degree = (Math.tan(Math.PI/180) * (57 * 10));
    // CRT_px2degree = (CRT_pixeldensity_px2mm  * CRT_mm2degree);
    expInfo['CRT_px2degree'] = 1024/366 * (Math.tan(Math.PI/180) * 57 * 10);
    
    // ratio between Lab CRT and online participant's monitor:
    // ratio_monitor2CRT = px2degree/CRT_px2degree;
    expInfo['ratio_monitor2CRT'] = Number.parseFloat(expInfo['px2degree'])/Number.parseFloat(expInfo['CRT_px2degree']);
    
    // To show whole search range 480x480 pixels on current windown size 1920x1080 and 1366x768 pixels (most common resolution)
    // the max ratio_monitor should be 768/480= 1.6
    
    // if redo virtual chinrest still provide a ratio higher than 1.6 (window size 768/ search range 480), just use 1.6 to continue:
    if ((expInfo["ratio_monitor2CRT"] <= 1.6)) {
        expInfo['PassVirtualChinrest'] = "Passed";
    }
    if ((expInfo["ratio_monitor2CRT"] > 1.6)) {
        expInfo['PassVirtualChinrest'] = "Failed";
    }
    
    // size of central fovea (6.7 degree in diameter, so radius should be 6.7/2)
    expInfo['foveaRadius_inPixel'] = Number.parseFloat(expInfo['px2degree'])*6.7/2;
    
    // the Routine "VirtualChinrest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _InstrRedo_key_allKeys;
var InstrRedoComponents;
function InstrRedoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'InstrRedo' ---
    t = 0;
    InstrRedoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('InstrRedo.started', globalClock.getTime());
    // Run 'Begin Routine' code from skip_offline_2
    continueRoutine = false;
    
    // Run 'Begin Routine' code from code_RedoInstr
    continueRoutine = false;
    if ((expInfo["ratio_monitor2CRT"] > 1.6)) {
        continueRoutine = true;
    }
    
    InstrRedo_key.keys = undefined;
    InstrRedo_key.rt = undefined;
    _InstrRedo_key_allKeys = [];
    // keep track of which components have finished
    InstrRedoComponents = [];
    InstrRedoComponents.push(InstrRedo_txt);
    InstrRedoComponents.push(InstrRedo_key);
    
    for (const thisComponent of InstrRedoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstrRedoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstrRedo' ---
    // get current time
    t = InstrRedoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *InstrRedo_txt* updates
    if (t >= 0.0 && InstrRedo_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrRedo_txt.tStart = t;  // (not accounting for frame time here)
      InstrRedo_txt.frameNStart = frameN;  // exact frame index
      
      InstrRedo_txt.setAutoDraw(true);
    }
    
    
    // *InstrRedo_key* updates
    if (t >= 0.0 && InstrRedo_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrRedo_key.tStart = t;  // (not accounting for frame time here)
      InstrRedo_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { InstrRedo_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { InstrRedo_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { InstrRedo_key.clearEvents(); });
    }
    
    if (InstrRedo_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = InstrRedo_key.getKeys({keyList: ['space'], waitRelease: false});
      _InstrRedo_key_allKeys = _InstrRedo_key_allKeys.concat(theseKeys);
      if (_InstrRedo_key_allKeys.length > 0) {
        InstrRedo_key.keys = _InstrRedo_key_allKeys[_InstrRedo_key_allKeys.length - 1].name;  // just the last key pressed
        InstrRedo_key.rt = _InstrRedo_key_allKeys[_InstrRedo_key_allKeys.length - 1].rt;
        InstrRedo_key.duration = _InstrRedo_key_allKeys[_InstrRedo_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstrRedoComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstrRedoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstrRedo' ---
    for (const thisComponent of InstrRedoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('InstrRedo.stopped', globalClock.getTime());
    InstrRedo_key.stop();
    // the Routine "InstrRedo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var VirtualChinrest_RedoComponents;
function VirtualChinrest_RedoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'VirtualChinrest_Redo' ---
    t = 0;
    VirtualChinrest_RedoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('VirtualChinrest_Redo.started', globalClock.getTime());
    // Run 'Begin Routine' code from skip_offline_redo
    continueRoutine = false;
    
    // Run 'Begin Routine' code from skip_redo
    // To show whole search range 600x600 pixels on current windown size 1920x1080 and 1366x768 pixels (most common resolution)
    // the max ratio_monitor should be 768/600= 1.28
    
    // if ratio is acceptance, then skip redo virutal chinrest
    if ((expInfo["ratio_monitor2CRT"] < 1.28)) {
        continueRoutine = false;
    }
    
    // This routine should not start straight away or the screen width and height
    // may be incorrect.
    
    expInfo['xRes'] = screen.width;
    expInfo['yRes'] = screen.height;
    console.log("screen xRes",expInfo['xRes']);
    console.log("screen yRes",expInfo['yRes']);
    
    //let src = ('demographics.html?xRes='+expInfo['xRes']+'&yRes='+expInfo['yRes']);
    let src = ('virtual_chinrest.html');
    
    continue_routine = true; // Routines can't be ended from within Begin Routine
    $(document).ready(function() {
        // Add custom contents from html file using an iframe:
        $('body').append('<div id="iframe-o" style="visibility: hidden; position: relative; display: table; margin: auto; overflow-x: hidden; overflow-y: scroll !important; -webkit-overflow-y-scrolling:touch !important;"><div id="iframe-m" style="display: table-cell; vertical-align: middle;"><div id="iframe-i" style="display: inline-block; width:100%; overflow-y: hidden; overflow-x: hidden;"><iframe id="iframe" src="'+src+'" frameborder="0" style="width: 100%; overflow-y: hidden; overflow-x: hidden; "></iframe></div></div></div>');
        $('#iframe').on('load',function(iframe){
            // Auto-adjust iframe size:
            $(this).contents().find('html').css({ 'display': 'table', 'width': '100%', 'overflow-x': 'hidden' });
            $('#iframe-o').height($(window).height()-20, true);
            $('#iframe-m').width($(this).contents().find('html').width()+100);
            $('#iframe-i').height ( Math.max ( $(this).contents().find('html').height()+20, $(window).height()-20 ), true );
            $(this).height($(this).contents().find('html').height());
            $('#iframe-o').css('visibility','visible');
            
            //if click submit button in a form:
            $(this).contents().find('form').on('submit',function(e){
                e.preventDefault();
                
                //expose the iframe to the window
                var iframe = $('#iframe');
                window.iframe = iframe; 
                // save viewing distance and pixel per mm into output file:
                psychoJS.experiment.addData('viewingdistance_cm', iframe[0].contentWindow.document.getElementById("info-h").innerText);
                psychoJS.experiment.addData('pixeldensity_px2mm', iframe[0].contentWindow.document.getElementById("info-lpd").innerText);
                // save into expInfo
                expInfo['viewingdistance_cm'] = iframe[0].contentWindow.document.getElementById("info-h").innerText;
                expInfo['pixeldensity_px2mm'] = iframe[0].contentWindow.document.getElementById("info-lpd").innerText;
                
                // Remove iframe and continue to next routine when done:
                $('#iframe-o').remove();
                continue_routine = false;
            });
            
        });
    });
    //$('#iframe').attr( 'src', function(i,val){ return val;} );
    // keep track of which components have finished
    VirtualChinrest_RedoComponents = [];
    VirtualChinrest_RedoComponents.push(loading_redo);
    
    for (const thisComponent of VirtualChinrest_RedoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function VirtualChinrest_RedoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'VirtualChinrest_Redo' ---
    // get current time
    t = VirtualChinrest_RedoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *loading_redo* updates
    if (t >= 0.0 && loading_redo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loading_redo.tStart = t;  // (not accounting for frame time here)
      loading_redo.frameNStart = frameN;  // exact frame index
      
      loading_redo.setAutoDraw(true);
    }
    
    continueRoutine = continue_routine;
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of VirtualChinrest_RedoComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VirtualChinrest_RedoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'VirtualChinrest_Redo' ---
    for (const thisComponent of VirtualChinrest_RedoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('VirtualChinrest_Redo.stopped', globalClock.getTime());
    // Using virtual Chinrest Results (viewing distance, pixel density) to estimate pixel per degree:
    // how many mm per degree
    psychoJS.experiment.addData('mm2degree',Math.tan(Math.PI/180) * (Number.parseFloat(expInfo['viewingdistance_cm']) * 10));
    expInfo['mm2degree'] = Math.tan(Math.PI/180) * (Number.parseFloat(expInfo['viewingdistance_cm']) * 10);
    // how many pixel per degree
    psychoJS.experiment.addData('px2degree', Number.parseFloat(expInfo['pixeldensity_px2mm']) * Number.parseFloat(expInfo['mm2degree']));
    expInfo['px2degree'] = Number.parseFloat(expInfo['pixeldensity_px2mm']) * Number.parseFloat(expInfo['mm2degree']);
    
    // if testing in Lab CRT with 36.6 cm height, 1024x768 resolution, and 57cm viewing distance: 
    // then 2.79 pixel per mm, 27.83 pixel per degree
    //var CRT_pixeldensity_px2mm = 1024/366;
    //var CRT_mm2degree = (Math.tan(Math.PI/180) * (57 * 10));
    //var CRT_px2degree = (CRT_pixeldensity_px2mm  * CRT_mm2degree);
    psychoJS.experiment.addData('CRT_px2degree',1024/366 * (Math.tan(Math.PI/180) * 57 * 10));
    expInfo['CRT_px2degree'] = 1024/366 * (Math.tan(Math.PI/180) * 57 * 10);
    
    // ratio between Lab CRT and online participant's monitor:
    //var ratio_monitor2CRT = px2degree/CRT_px2degree;
    psychoJS.experiment.addData('ratio_monitor2CRT', Number.parseFloat(expInfo['px2degree'])/Number.parseFloat(expInfo['CRT_px2degree']));
    expInfo['ratio_monitor2CRT'] = Number.parseFloat(expInfo['px2degree'])/Number.parseFloat(expInfo['CRT_px2degree']);
    
    // To show whole search range 600x600 pixels on current windown size 1920x1080 and 1366x768 pixels (most common resolution)
    // the max ratio_monitor should be 768/600= 1.28
    
    // after redo, if ratio is still larger than 1.28 , then just use 1.28
    if ((expInfo["ratio_monitor2CRT"] > 1.28)) {
        psychoJS.experiment.addData('Redo_virtualChinrest', "failed");
        expInfo["ratio_monitor2CRT"] = 1.28;
    }
    
    
    // size of central fovea (6.7 degree in diameter)
    psychoJS.experiment.addData('foveaRadius_inPixel',Number.parseFloat(expInfo['px2degree'])*6.7/2);
    expInfo['foveaRadius_inPixel'] = Number.parseFloat(expInfo['px2degree'])*6.7/2;
    
    // the Routine "VirtualChinrest_Redo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_instr1key_allKeys;
var Instruction1Components;
function Instruction1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction1' ---
    t = 0;
    Instruction1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instruction1.started', globalClock.getTime());
    key_instr1key.keys = undefined;
    key_instr1key.rt = undefined;
    _key_instr1key_allKeys = [];
    // keep track of which components have finished
    Instruction1Components = [];
    Instruction1Components.push(instr1_key);
    Instruction1Components.push(key_instr1key);
    
    for (const thisComponent of Instruction1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction1' ---
    // get current time
    t = Instruction1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr1_key* updates
    if (t >= 0.0 && instr1_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr1_key.tStart = t;  // (not accounting for frame time here)
      instr1_key.frameNStart = frameN;  // exact frame index
      
      instr1_key.setAutoDraw(true);
    }
    
    
    // *key_instr1key* updates
    if (t >= 1 && key_instr1key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_instr1key.tStart = t;  // (not accounting for frame time here)
      key_instr1key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_instr1key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_instr1key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_instr1key.clearEvents(); });
    }
    
    if (key_instr1key.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_instr1key.getKeys({keyList: ['space'], waitRelease: false});
      _key_instr1key_allKeys = _key_instr1key_allKeys.concat(theseKeys);
      if (_key_instr1key_allKeys.length > 0) {
        key_instr1key.keys = _key_instr1key_allKeys[_key_instr1key_allKeys.length - 1].name;  // just the last key pressed
        key_instr1key.rt = _key_instr1key_allKeys[_key_instr1key_allKeys.length - 1].rt;
        key_instr1key.duration = _key_instr1key_allKeys[_key_instr1key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction1' ---
    for (const thisComponent of Instruction1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instruction1.stopped', globalClock.getTime());
    key_instr1key.stop();
    // the Routine "Instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var keyPracLoop;
function keyPracLoopLoopBegin(keyPracLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    keyPracLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Seq_keyprac.xlsx',
      seed: undefined, name: 'keyPracLoop'
    });
    psychoJS.experiment.addLoop(keyPracLoop); // add the loop to the experiment
    currentLoop = keyPracLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisKeyPracLoop of keyPracLoop) {
      snapshot = keyPracLoop.getSnapshot();
      keyPracLoopLoopScheduler.add(importConditions(snapshot));
      keyPracLoopLoopScheduler.add(keyPracticeRoutineBegin(snapshot));
      keyPracLoopLoopScheduler.add(keyPracticeRoutineEachFrame());
      keyPracLoopLoopScheduler.add(keyPracticeRoutineEnd(snapshot));
      keyPracLoopLoopScheduler.add(keyPracFeedbackRoutineBegin(snapshot));
      keyPracLoopLoopScheduler.add(keyPracFeedbackRoutineEachFrame());
      keyPracLoopLoopScheduler.add(keyPracFeedbackRoutineEnd(snapshot));
      keyPracLoopLoopScheduler.add(keyPracLoopLoopEndIteration(keyPracLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function keyPracLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(keyPracLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function keyPracLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialsPractice;
function trialsPracticeLoopBegin(trialsPracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsPractice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Seq_practice.xlsx',
      seed: undefined, name: 'trialsPractice'
    });
    psychoJS.experiment.addLoop(trialsPractice); // add the loop to the experiment
    currentLoop = trialsPractice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsPractice of trialsPractice) {
      snapshot = trialsPractice.getSnapshot();
      trialsPracticeLoopScheduler.add(importConditions(snapshot));
      trialsPracticeLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsPracticeLoopScheduler.add(fixationRoutineEachFrame());
      trialsPracticeLoopScheduler.add(fixationRoutineEnd(snapshot));
      trialsPracticeLoopScheduler.add(greenFixationRoutineBegin(snapshot));
      trialsPracticeLoopScheduler.add(greenFixationRoutineEachFrame());
      trialsPracticeLoopScheduler.add(greenFixationRoutineEnd(snapshot));
      trialsPracticeLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsPracticeLoopScheduler.add(trialRoutineEachFrame());
      trialsPracticeLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsPracticeLoopScheduler.add(trialFeedbackRoutineBegin(snapshot));
      trialsPracticeLoopScheduler.add(trialFeedbackRoutineEachFrame());
      trialsPracticeLoopScheduler.add(trialFeedbackRoutineEnd(snapshot));
      trialsPracticeLoopScheduler.add(trialsPracticeLoopEndIteration(trialsPracticeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsPracticeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsPractice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsPracticeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: parameterfile,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixationRoutineEachFrame());
      trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
      trialsLoopScheduler.add(greenFixationRoutineBegin(snapshot));
      trialsLoopScheduler.add(greenFixationRoutineEachFrame());
      trialsLoopScheduler.add(greenFixationRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialFeedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialFeedbackRoutineEachFrame());
      trialsLoopScheduler.add(trialFeedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(TakeABreakRoutineBegin(snapshot));
      trialsLoopScheduler.add(TakeABreakRoutineEachFrame());
      trialsLoopScheduler.add(TakeABreakRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Testingtrials;
function TestingtrialsLoopBegin(TestingtrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Testingtrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: testingfile,
      seed: undefined, name: 'Testingtrials'
    });
    psychoJS.experiment.addLoop(Testingtrials); // add the loop to the experiment
    currentLoop = Testingtrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTestingtrial of Testingtrials) {
      snapshot = Testingtrials.getSnapshot();
      TestingtrialsLoopScheduler.add(importConditions(snapshot));
      TestingtrialsLoopScheduler.add(fixationRoutineBegin(snapshot));
      TestingtrialsLoopScheduler.add(fixationRoutineEachFrame());
      TestingtrialsLoopScheduler.add(fixationRoutineEnd(snapshot));
      TestingtrialsLoopScheduler.add(greenFixationRoutineBegin(snapshot));
      TestingtrialsLoopScheduler.add(greenFixationRoutineEachFrame());
      TestingtrialsLoopScheduler.add(greenFixationRoutineEnd(snapshot));
      TestingtrialsLoopScheduler.add(displayTestingPhaseRoutineBegin(snapshot));
      TestingtrialsLoopScheduler.add(displayTestingPhaseRoutineEachFrame());
      TestingtrialsLoopScheduler.add(displayTestingPhaseRoutineEnd(snapshot));
      TestingtrialsLoopScheduler.add(trialFeedbackRoutineBegin(snapshot));
      TestingtrialsLoopScheduler.add(trialFeedbackRoutineEachFrame());
      TestingtrialsLoopScheduler.add(trialFeedbackRoutineEnd(snapshot));
      TestingtrialsLoopScheduler.add(TakeABreak2RoutineBegin(snapshot));
      TestingtrialsLoopScheduler.add(TakeABreak2RoutineEachFrame());
      TestingtrialsLoopScheduler.add(TakeABreak2RoutineEnd(snapshot));
      TestingtrialsLoopScheduler.add(TestingtrialsLoopEndIteration(TestingtrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function TestingtrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Testingtrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function TestingtrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var RTtrials;
function RTtrialsLoopBegin(RTtrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    RTtrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: rtfile,
      seed: undefined, name: 'RTtrials'
    });
    psychoJS.experiment.addLoop(RTtrials); // add the loop to the experiment
    currentLoop = RTtrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRTtrial of RTtrials) {
      snapshot = RTtrials.getSnapshot();
      RTtrialsLoopScheduler.add(importConditions(snapshot));
      RTtrialsLoopScheduler.add(fixation_RTRoutineBegin(snapshot));
      RTtrialsLoopScheduler.add(fixation_RTRoutineEachFrame());
      RTtrialsLoopScheduler.add(fixation_RTRoutineEnd(snapshot));
      RTtrialsLoopScheduler.add(displayRTRoutineBegin(snapshot));
      RTtrialsLoopScheduler.add(displayRTRoutineEachFrame());
      RTtrialsLoopScheduler.add(displayRTRoutineEnd(snapshot));
      RTtrialsLoopScheduler.add(RTtrialsLoopEndIteration(RTtrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function RTtrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(RTtrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function RTtrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _key_keyprac_allKeys;
var keyPracticeComponents;
function keyPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'keyPractice' ---
    t = 0;
    keyPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('keyPractice.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_keyprac
    hintlocation = (255 * expInfo["ratio_monitor2CRT"]);
    
    letterT.setOri(targOrientdeg);
    keyHint.setPos([0, hintlocation]);
    key_keyprac.keys = undefined;
    key_keyprac.rt = undefined;
    _key_keyprac_allKeys = [];
    // keep track of which components have finished
    keyPracticeComponents = [];
    keyPracticeComponents.push(fixation_keyprac);
    keyPracticeComponents.push(letterT);
    keyPracticeComponents.push(keyHint);
    keyPracticeComponents.push(key_keyprac);
    
    for (const thisComponent of keyPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function keyPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'keyPractice' ---
    // get current time
    t = keyPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_keyprac* updates
    if (t >= 0.0 && fixation_keyprac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_keyprac.tStart = t;  // (not accounting for frame time here)
      fixation_keyprac.frameNStart = frameN;  // exact frame index
      
      fixation_keyprac.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_keyprac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_keyprac.setAutoDraw(false);
    }
    
    // *letterT* updates
    if (t >= 0.5 && letterT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      letterT.tStart = t;  // (not accounting for frame time here)
      letterT.frameNStart = frameN;  // exact frame index
      
      letterT.setAutoDraw(true);
    }
    
    
    // *keyHint* updates
    if (t >= 0.5 && keyHint.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyHint.tStart = t;  // (not accounting for frame time here)
      keyHint.frameNStart = frameN;  // exact frame index
      
      keyHint.setAutoDraw(true);
    }
    
    
    // *key_keyprac* updates
    if (t >= 0.5 && key_keyprac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_keyprac.tStart = t;  // (not accounting for frame time here)
      key_keyprac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_keyprac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_keyprac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_keyprac.clearEvents(); });
    }
    
    if (key_keyprac.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_keyprac.getKeys({keyList: ['a', 's'], waitRelease: false});
      _key_keyprac_allKeys = _key_keyprac_allKeys.concat(theseKeys);
      if (_key_keyprac_allKeys.length > 0) {
        key_keyprac.keys = _key_keyprac_allKeys[0].name;  // just the first key pressed
        key_keyprac.rt = _key_keyprac_allKeys[0].rt;
        key_keyprac.duration = _key_keyprac_allKeys[0].duration;
        // was this correct?
        if (key_keyprac.keys == corrAnswer) {
            key_keyprac.corr = 1;
        } else {
            key_keyprac.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of keyPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var keyprac_fbtext;
var keyprac_fbcolor;
var keyprac_fbdur;
function keyPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'keyPractice' ---
    for (const thisComponent of keyPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('keyPractice.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_keyprac
    if ((key_keyprac.corr === 1)) {
        keyprac_fbtext = "correct!";
        keyprac_fbcolor = "green";
        keyprac_fbdur = 0.5;
    } else {
        keyprac_fbtext = "incorrect!";
        keyprac_fbcolor = "red";
        keyprac_fbdur = 0.5;
    }
    
    // was no response the correct answer?!
    if (key_keyprac.keys === undefined) {
      if (['None','none',undefined].includes(corrAnswer)) {
         key_keyprac.corr = 1;  // correct non-response
      } else {
         key_keyprac.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_keyprac.corr, level);
    }
    psychoJS.experiment.addData('key_keyprac.keys', key_keyprac.keys);
    psychoJS.experiment.addData('key_keyprac.corr', key_keyprac.corr);
    if (typeof key_keyprac.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_keyprac.rt', key_keyprac.rt);
        psychoJS.experiment.addData('key_keyprac.duration', key_keyprac.duration);
        routineTimer.reset();
        }
    
    key_keyprac.stop();
    // the Routine "keyPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var keyPracFeedbackComponents;
function keyPracFeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'keyPracFeedback' ---
    t = 0;
    keyPracFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('keyPracFeedback.started', globalClock.getTime());
    keyFeedback.setColor(new util.Color(keyprac_fbcolor));
    keyFeedback.setText(keyprac_fbtext);
    // keep track of which components have finished
    keyPracFeedbackComponents = [];
    keyPracFeedbackComponents.push(keyFeedback);
    
    for (const thisComponent of keyPracFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function keyPracFeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'keyPracFeedback' ---
    // get current time
    t = keyPracFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *keyFeedback* updates
    if (t >= 0.0 && keyFeedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyFeedback.tStart = t;  // (not accounting for frame time here)
      keyFeedback.frameNStart = frameN;  // exact frame index
      
      keyFeedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + keyprac_fbdur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (keyFeedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      keyFeedback.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of keyPracFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function keyPracFeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'keyPracFeedback' ---
    for (const thisComponent of keyPracFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('keyPracFeedback.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_endkeyprac
    sumaccKeyPrac = (sumaccKeyPrac + key_keyprac.corr);
    if ((sumaccKeyPrac >= 6)) {
        keyPracLoop.finished = true;
    }
    
    // the Routine "keyPracFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_instr2search_allKeys;
var Instruction2Components;
function Instruction2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction2' ---
    t = 0;
    Instruction2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instruction2.started', globalClock.getTime());
    key_instr2search.keys = undefined;
    key_instr2search.rt = undefined;
    _key_instr2search_allKeys = [];
    // keep track of which components have finished
    Instruction2Components = [];
    Instruction2Components.push(instr2_search);
    Instruction2Components.push(key_instr2search);
    
    for (const thisComponent of Instruction2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction2' ---
    // get current time
    t = Instruction2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr2_search* updates
    if (t >= 0.0 && instr2_search.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr2_search.tStart = t;  // (not accounting for frame time here)
      instr2_search.frameNStart = frameN;  // exact frame index
      
      instr2_search.setAutoDraw(true);
    }
    
    
    // *key_instr2search* updates
    if (t >= 1 && key_instr2search.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_instr2search.tStart = t;  // (not accounting for frame time here)
      key_instr2search.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_instr2search.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_instr2search.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_instr2search.clearEvents(); });
    }
    
    if (key_instr2search.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_instr2search.getKeys({keyList: ['space'], waitRelease: false});
      _key_instr2search_allKeys = _key_instr2search_allKeys.concat(theseKeys);
      if (_key_instr2search_allKeys.length > 0) {
        key_instr2search.keys = _key_instr2search_allKeys[_key_instr2search_allKeys.length - 1].name;  // just the last key pressed
        key_instr2search.rt = _key_instr2search_allKeys[_key_instr2search_allKeys.length - 1].rt;
        key_instr2search.duration = _key_instr2search_allKeys[_key_instr2search_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction2' ---
    for (const thisComponent of Instruction2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instruction2.stopped', globalClock.getTime());
    key_instr2search.stop();
    // the Routine "Instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_instr3fix_allKeys;
var Instruction3Components;
function Instruction3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction3' ---
    t = 0;
    Instruction3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instruction3.started', globalClock.getTime());
    key_instr3fix.keys = undefined;
    key_instr3fix.rt = undefined;
    _key_instr3fix_allKeys = [];
    // keep track of which components have finished
    Instruction3Components = [];
    Instruction3Components.push(instr3_fix);
    Instruction3Components.push(key_instr3fix);
    
    for (const thisComponent of Instruction3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction3' ---
    // get current time
    t = Instruction3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr3_fix* updates
    if (t >= 0.0 && instr3_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr3_fix.tStart = t;  // (not accounting for frame time here)
      instr3_fix.frameNStart = frameN;  // exact frame index
      
      instr3_fix.setAutoDraw(true);
    }
    
    
    // *key_instr3fix* updates
    if (t >= 1 && key_instr3fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_instr3fix.tStart = t;  // (not accounting for frame time here)
      key_instr3fix.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_instr3fix.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_instr3fix.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_instr3fix.clearEvents(); });
    }
    
    if (key_instr3fix.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_instr3fix.getKeys({keyList: ['space'], waitRelease: false});
      _key_instr3fix_allKeys = _key_instr3fix_allKeys.concat(theseKeys);
      if (_key_instr3fix_allKeys.length > 0) {
        key_instr3fix.keys = _key_instr3fix_allKeys[_key_instr3fix_allKeys.length - 1].name;  // just the last key pressed
        key_instr3fix.rt = _key_instr3fix_allKeys[_key_instr3fix_allKeys.length - 1].rt;
        key_instr3fix.duration = _key_instr3fix_allKeys[_key_instr3fix_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction3' ---
    for (const thisComponent of Instruction3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instruction3.stopped', globalClock.getTime());
    key_instr3fix.stop();
    // the Routine "Instruction3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fixationStartTime;
var gotValidClick;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_fixinitial
    psychoJS.window.mouseVisible = true;
    if ((phase === "practice")) {
        fixationStartTime = 4;
    } else {
        fixationStartTime = 10000;
    }
    psychoJS.window.mouseVisible = true;
    fixsize = (28 * expInfo["ratio_monitor2CRT"]);
    hintlocation = (255 * expInfo["ratio_monitor2CRT"]);
    
    fixationPoint.setSize([fixsize, fixsize]);
    fixationHint.setPos([0, hintlocation]);
    // setup some python lists for storing info about the mouseintial
    // current position of the mouse:
    mouseintial.x = [];
    mouseintial.y = [];
    mouseintial.leftButton = [];
    mouseintial.midButton = [];
    mouseintial.rightButton = [];
    mouseintial.time = [];
    mouseintial.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouseintial.mouseClock.reset();
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(fixationPoint);
    fixationComponents.push(fixationHint);
    fixationComponents.push(mouseintial);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixationPoint* updates
    if (t >= 0.0 && fixationPoint.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationPoint.tStart = t;  // (not accounting for frame time here)
      fixationPoint.frameNStart = frameN;  // exact frame index
      
      fixationPoint.setAutoDraw(true);
    }
    
    
    // *fixationHint* updates
    if (t >= fixationStartTime && fixationHint.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationHint.tStart = t;  // (not accounting for frame time here)
      fixationHint.frameNStart = frameN;  // exact frame index
      
      fixationHint.setAutoDraw(true);
    }
    
    // *mouseintial* updates
    if (t >= 0 && mouseintial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseintial.tStart = t;  // (not accounting for frame time here)
      mouseintial.frameNStart = frameN;  // exact frame index
      
      mouseintial.status = PsychoJS.Status.STARTED;
      prevButtonState = mouseintial.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseintial.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseintial.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [fixationPoint]) {
            if (obj.contains(mouseintial)) {
              gotValidClick = true;
              mouseintial.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouseintial.getPos();
          mouseintial.x.push(_mouseXYs[0]);
          mouseintial.y.push(_mouseXYs[1]);
          mouseintial.leftButton.push(_mouseButtons[0]);
          mouseintial.midButton.push(_mouseButtons[1]);
          mouseintial.rightButton.push(_mouseButtons[2]);
          mouseintial.time.push(mouseintial.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var mouselocation;
function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fixation.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_fixinitial
    mouselocation = [0, 0];
    psychoJS.experiment.addData("fixationSize", fixsize);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouseintial.x) {  psychoJS.experiment.addData('mouseintial.x', mouseintial.x[0])};
    if (mouseintial.y) {  psychoJS.experiment.addData('mouseintial.y', mouseintial.y[0])};
    if (mouseintial.leftButton) {  psychoJS.experiment.addData('mouseintial.leftButton', mouseintial.leftButton[0])};
    if (mouseintial.midButton) {  psychoJS.experiment.addData('mouseintial.midButton', mouseintial.midButton[0])};
    if (mouseintial.rightButton) {  psychoJS.experiment.addData('mouseintial.rightButton', mouseintial.rightButton[0])};
    if (mouseintial.time) {  psychoJS.experiment.addData('mouseintial.time', mouseintial.time[0])};
    if (mouseintial.clicked_name) {  psychoJS.experiment.addData('mouseintial.clicked_name', mouseintial.clicked_name[0])};
    
    // the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var greenFixationComponents;
function greenFixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'greenFixation' ---
    t = 0;
    greenFixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.100000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('greenFixation.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_fixinitial_2
    psychoJS.window.mouseVisible = true;
    if ((phase === "practice")) {
        fixationStartTime = 4;
    } else {
        fixationStartTime = 10000;
    }
    psychoJS.window.mouseVisible = true;
    fixsize = (28 * expInfo["ratio_monitor2CRT"]);
    hintlocation = (255 * expInfo["ratio_monitor2CRT"]);
    
    fixationPoint_2.setSize([fixsize, fixsize]);
    // keep track of which components have finished
    greenFixationComponents = [];
    greenFixationComponents.push(fixationPoint_2);
    
    for (const thisComponent of greenFixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function greenFixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'greenFixation' ---
    // get current time
    t = greenFixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixationPoint_2* updates
    if (t >= 0.0 && fixationPoint_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationPoint_2.tStart = t;  // (not accounting for frame time here)
      fixationPoint_2.frameNStart = frameN;  // exact frame index
      
      fixationPoint_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixationPoint_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationPoint_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of greenFixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function greenFixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'greenFixation' ---
    for (const thisComponent of greenFixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('greenFixation.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_fixinitial_2
    mouselocation = [0, 0];
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var whichframe;
var mouselocationlistx;
var mouselocationlisty;
var whichframelist;
var searchHintStartTime;
var searchHintText;
var startApertureTime;
var _key_respMain_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_initial
    psychoJS.window.mouseVisible = true;
    mouselocation = [0, 0];
    whichframe = 0;
    mouselocationlistx = [];
    mouselocationlisty = [];
    whichframelist = [];
    if ((phase === "practice")) {
        searchHintStartTime = 0;
        if ((block === 0)) {
            searchHintText = "Please find letter T and report its direction";
        } else {
            searchHintText = "Please find letter T and report its direction";
        }
    } else {
        searchHintStartTime = 10000;
    }
    if ((block === 0)) {
        startApertureTime = 10000;
    } else {
        startApertureTime = 10000;
    }
    lettersize = (28 * expInfo["ratio_monitor2CRT"]);
    aperturesize = (8000 * expInfo["ratio_monitor2CRT"]);
    searchsize = (482 * expInfo["ratio_monitor2CRT"]);
    newtlocx = (tlocx * expInfo["ratio_monitor2CRT"]);
    newtlocy = (tlocy * expInfo["ratio_monitor2CRT"]);
    newd1x = (d1x * expInfo["ratio_monitor2CRT"]);
    newd1y = (d1y * expInfo["ratio_monitor2CRT"]);
    newd2x = (d2x * expInfo["ratio_monitor2CRT"]);
    newd2y = (d2y * expInfo["ratio_monitor2CRT"]);
    newd3x = (d3x * expInfo["ratio_monitor2CRT"]);
    newd3y = (d3y * expInfo["ratio_monitor2CRT"]);
    newd4x = (d4x * expInfo["ratio_monitor2CRT"]);
    newd4y = (d4y * expInfo["ratio_monitor2CRT"]);
    newd5x = (d5x * expInfo["ratio_monitor2CRT"]);
    newd5y = (d5y * expInfo["ratio_monitor2CRT"]);
    newd6x = (d6x * expInfo["ratio_monitor2CRT"]);
    newd6y = (d6y * expInfo["ratio_monitor2CRT"]);
    newd7x = (d7x * expInfo["ratio_monitor2CRT"]);
    newd7y = (d7y * expInfo["ratio_monitor2CRT"]);
    newd8x = (d8x * expInfo["ratio_monitor2CRT"]);
    newd8y = (d8y * expInfo["ratio_monitor2CRT"]);
    newd9x = (d9x * expInfo["ratio_monitor2CRT"]);
    newd9y = (d9y * expInfo["ratio_monitor2CRT"]);
    newd10x = (d10x * expInfo["ratio_monitor2CRT"]);
    newd10y = (d10y * expInfo["ratio_monitor2CRT"]);
    newd11x = (d11x * expInfo["ratio_monitor2CRT"]);
    newd11y = (d11y * expInfo["ratio_monitor2CRT"]);
    hintlocation = (255 * expInfo["ratio_monitor2CRT"]);
    
    background.setSize([searchsize, searchsize]);
    imageT.setPos([newtlocx, newtlocy]);
    imageT.setSize([lettersize, lettersize]);
    imageT.setOri(targOrientdeg);
    imageL1.setPos([newd1x, newd1y]);
    imageL1.setSize([lettersize, lettersize]);
    imageL1.setOri(d1Orient);
    imageL2.setPos([newd2x, newd2y]);
    imageL2.setSize([lettersize, lettersize]);
    imageL2.setOri(d2Orient);
    imageL3.setPos([newd3x, newd3y]);
    imageL3.setSize([lettersize, lettersize]);
    imageL3.setOri(d3Orient);
    imageL4.setPos([newd4x, newd4y]);
    imageL4.setSize([lettersize, lettersize]);
    imageL4.setOri(d4Orient);
    imageL5.setPos([newd5x, newd5y]);
    imageL5.setSize([lettersize, lettersize]);
    imageL5.setOri(d5Orient);
    imageL6.setPos([newd6x, newd6y]);
    imageL6.setSize([lettersize, lettersize]);
    imageL6.setOri(d6Orient);
    imageL7.setPos([newd7x, newd7y]);
    imageL7.setSize([lettersize, lettersize]);
    imageL7.setOri(d7Orient);
    imageL8.setPos([newd8x, newd8y]);
    imageL8.setSize([lettersize, lettersize]);
    imageL8.setOri(d8Orient);
    imageL9.setPos([newd9x, newd9y]);
    imageL9.setSize([lettersize, lettersize]);
    imageL9.setOri(d9Orient);
    imageL10.setPos([newd10x, newd10y]);
    imageL10.setSize([lettersize, lettersize]);
    imageL10.setOri(d10Orient);
    imageL11.setPos([newd11x, newd11y]);
    imageL11.setSize([lettersize, lettersize]);
    imageL11.setOri(d11Orient);
    imageAperture.setSize([aperturesize, aperturesize]);
    CenterAperture.setPos([0, 0]);
    CenterAperture.setSize([aperturesize, aperturesize]);
    searchHint.setPos([0, hintlocation]);
    searchHint.setText(searchHintText);
    key_respMain.keys = undefined;
    key_respMain.rt = undefined;
    _key_respMain_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(background);
    trialComponents.push(imageT);
    trialComponents.push(imageL1);
    trialComponents.push(imageL2);
    trialComponents.push(imageL3);
    trialComponents.push(imageL4);
    trialComponents.push(imageL5);
    trialComponents.push(imageL6);
    trialComponents.push(imageL7);
    trialComponents.push(imageL8);
    trialComponents.push(imageL9);
    trialComponents.push(imageL10);
    trialComponents.push(imageL11);
    trialComponents.push(imageAperture);
    trialComponents.push(CenterAperture);
    trialComponents.push(searchHint);
    trialComponents.push(key_respMain);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background* updates
    if (t >= 0.0 && background.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background.tStart = t;  // (not accounting for frame time here)
      background.frameNStart = frameN;  // exact frame index
      
      background.setAutoDraw(true);
    }
    
    
    // *imageT* updates
    if (t >= 0 && imageT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageT.tStart = t;  // (not accounting for frame time here)
      imageT.frameNStart = frameN;  // exact frame index
      
      imageT.setAutoDraw(true);
    }
    
    
    // *imageL1* updates
    if (t >= 0 && imageL1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL1.tStart = t;  // (not accounting for frame time here)
      imageL1.frameNStart = frameN;  // exact frame index
      
      imageL1.setAutoDraw(true);
    }
    
    
    // *imageL2* updates
    if (t >= 0 && imageL2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL2.tStart = t;  // (not accounting for frame time here)
      imageL2.frameNStart = frameN;  // exact frame index
      
      imageL2.setAutoDraw(true);
    }
    
    
    // *imageL3* updates
    if (t >= 0 && imageL3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL3.tStart = t;  // (not accounting for frame time here)
      imageL3.frameNStart = frameN;  // exact frame index
      
      imageL3.setAutoDraw(true);
    }
    
    
    // *imageL4* updates
    if (t >= 0 && imageL4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL4.tStart = t;  // (not accounting for frame time here)
      imageL4.frameNStart = frameN;  // exact frame index
      
      imageL4.setAutoDraw(true);
    }
    
    
    // *imageL5* updates
    if (t >= 0 && imageL5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL5.tStart = t;  // (not accounting for frame time here)
      imageL5.frameNStart = frameN;  // exact frame index
      
      imageL5.setAutoDraw(true);
    }
    
    
    // *imageL6* updates
    if (t >= 0 && imageL6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL6.tStart = t;  // (not accounting for frame time here)
      imageL6.frameNStart = frameN;  // exact frame index
      
      imageL6.setAutoDraw(true);
    }
    
    
    // *imageL7* updates
    if (t >= 0 && imageL7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL7.tStart = t;  // (not accounting for frame time here)
      imageL7.frameNStart = frameN;  // exact frame index
      
      imageL7.setAutoDraw(true);
    }
    
    
    // *imageL8* updates
    if (t >= 0 && imageL8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL8.tStart = t;  // (not accounting for frame time here)
      imageL8.frameNStart = frameN;  // exact frame index
      
      imageL8.setAutoDraw(true);
    }
    
    
    // *imageL9* updates
    if (t >= 0 && imageL9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL9.tStart = t;  // (not accounting for frame time here)
      imageL9.frameNStart = frameN;  // exact frame index
      
      imageL9.setAutoDraw(true);
    }
    
    
    // *imageL10* updates
    if (t >= 0 && imageL10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL10.tStart = t;  // (not accounting for frame time here)
      imageL10.frameNStart = frameN;  // exact frame index
      
      imageL10.setAutoDraw(true);
    }
    
    
    // *imageL11* updates
    if (t >= 0 && imageL11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL11.tStart = t;  // (not accounting for frame time here)
      imageL11.frameNStart = frameN;  // exact frame index
      
      imageL11.setAutoDraw(true);
    }
    
    
    if (imageAperture.status === PsychoJS.Status.STARTED){ // only update if being drawn
      imageAperture.setPos(mouselocation, false);
    }
    
    // *imageAperture* updates
    if (t >= startApertureTime && imageAperture.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageAperture.tStart = t;  // (not accounting for frame time here)
      imageAperture.frameNStart = frameN;  // exact frame index
      
      imageAperture.setAutoDraw(true);
    }
    
    
    // *CenterAperture* updates
    if (t >= startApertureTime && CenterAperture.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CenterAperture.tStart = t;  // (not accounting for frame time here)
      CenterAperture.frameNStart = frameN;  // exact frame index
      
      CenterAperture.setAutoDraw(true);
    }
    
    if (CenterAperture.status === PsychoJS.Status.STARTED && frameN >= (CenterAperture.frameNStart + 1)) {
      CenterAperture.setAutoDraw(false);
    }
    
    // *searchHint* updates
    if (t >= searchHintStartTime && searchHint.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      searchHint.tStart = t;  // (not accounting for frame time here)
      searchHint.frameNStart = frameN;  // exact frame index
      
      searchHint.setAutoDraw(true);
    }
    
    
    // *key_respMain* updates
    if (t >= 0 && key_respMain.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respMain.tStart = t;  // (not accounting for frame time here)
      key_respMain.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respMain.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respMain.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respMain.clearEvents(); });
    }
    
    if (key_respMain.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respMain.getKeys({keyList: ['a', 's'], waitRelease: false});
      _key_respMain_allKeys = _key_respMain_allKeys.concat(theseKeys);
      if (_key_respMain_allKeys.length > 0) {
        key_respMain.keys = _key_respMain_allKeys[0].name;  // just the first key pressed
        key_respMain.rt = _key_respMain_allKeys[0].rt;
        key_respMain.duration = _key_respMain_allKeys[0].duration;
        // was this correct?
        if (key_respMain.keys == corrAnswer) {
            key_respMain.corr = 1;
        } else {
            key_respMain.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var fbtext;
var fbcolor;
var fbdur;
function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_initial
    psychoJS.experiment.addData("letterSize", lettersize);
    psychoJS.experiment.addData("apertureSize", aperturesize);
    psychoJS.experiment.addData("searchsize", searchsize);
    
    // was no response the correct answer?!
    if (key_respMain.keys === undefined) {
      if (['None','none',undefined].includes(corrAnswer)) {
         key_respMain.corr = 1;  // correct non-response
      } else {
         key_respMain.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respMain.corr, level);
    }
    psychoJS.experiment.addData('key_respMain.keys', key_respMain.keys);
    psychoJS.experiment.addData('key_respMain.corr', key_respMain.corr);
    if (typeof key_respMain.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respMain.rt', key_respMain.rt);
        psychoJS.experiment.addData('key_respMain.duration', key_respMain.duration);
        routineTimer.reset();
        }
    
    key_respMain.stop();
    // Run 'End Routine' code from code_end
    mouselocation = [0, 0];
    if ((key_respMain.corr === 1)) {
        fbtext = "correct!";
        fbcolor = "green";
        fbdur = 0.2;
    } else {
        fbtext = "incorrect!";
        fbcolor = "red";
        fbdur = 4;
    }
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialFeedbackComponents;
function trialFeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trialFeedback' ---
    t = 0;
    trialFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trialFeedback.started', globalClock.getTime());
    textFeedback.setColor(new util.Color(fbcolor));
    textFeedback.setText(fbtext);
    // keep track of which components have finished
    trialFeedbackComponents = [];
    trialFeedbackComponents.push(textFeedback);
    
    for (const thisComponent of trialFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialFeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trialFeedback' ---
    // get current time
    t = trialFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textFeedback* updates
    if (t >= 0.0 && textFeedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textFeedback.tStart = t;  // (not accounting for frame time here)
      textFeedback.frameNStart = frameN;  // exact frame index
      
      textFeedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fbdur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textFeedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textFeedback.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialFeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trialFeedback' ---
    for (const thisComponent of trialFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trialFeedback.stopped', globalClock.getTime());
    // the Routine "trialFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_checkInstr_allKeys;
var CheckInstrComponents;
function CheckInstrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'CheckInstr' ---
    t = 0;
    CheckInstrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('CheckInstr.started', globalClock.getTime());
    key_checkInstr.keys = undefined;
    key_checkInstr.rt = undefined;
    _key_checkInstr_allKeys = [];
    // keep track of which components have finished
    CheckInstrComponents = [];
    CheckInstrComponents.push(text_checkInstr);
    CheckInstrComponents.push(checkIntr_example);
    CheckInstrComponents.push(key_checkInstr);
    
    for (const thisComponent of CheckInstrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function CheckInstrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'CheckInstr' ---
    // get current time
    t = CheckInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_checkInstr* updates
    if (t >= 0 && text_checkInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_checkInstr.tStart = t;  // (not accounting for frame time here)
      text_checkInstr.frameNStart = frameN;  // exact frame index
      
      text_checkInstr.setAutoDraw(true);
    }
    
    
    // *checkIntr_example* updates
    if (t >= 0 && checkIntr_example.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      checkIntr_example.tStart = t;  // (not accounting for frame time here)
      checkIntr_example.frameNStart = frameN;  // exact frame index
      
      checkIntr_example.setAutoDraw(true);
    }
    
    
    // *key_checkInstr* updates
    if (t >= 0 && key_checkInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_checkInstr.tStart = t;  // (not accounting for frame time here)
      key_checkInstr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_checkInstr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_checkInstr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_checkInstr.clearEvents(); });
    }
    
    if (key_checkInstr.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_checkInstr.getKeys({keyList: ['a', 's'], waitRelease: false});
      _key_checkInstr_allKeys = _key_checkInstr_allKeys.concat(theseKeys);
      if (_key_checkInstr_allKeys.length > 0) {
        key_checkInstr.keys = _key_checkInstr_allKeys[_key_checkInstr_allKeys.length - 1].name;  // just the last key pressed
        key_checkInstr.rt = _key_checkInstr_allKeys[_key_checkInstr_allKeys.length - 1].rt;
        key_checkInstr.duration = _key_checkInstr_allKeys[_key_checkInstr_allKeys.length - 1].duration;
        // was this correct?
        if (key_checkInstr.keys == 'a') {
            key_checkInstr.corr = 1;
        } else {
            key_checkInstr.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of CheckInstrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var fbtext_checkInstr;
function CheckInstrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'CheckInstr' ---
    for (const thisComponent of CheckInstrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('CheckInstr.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_checkInstr.keys === undefined) {
      if (['None','none',undefined].includes('a')) {
         key_checkInstr.corr = 1;  // correct non-response
      } else {
         key_checkInstr.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_checkInstr.corr, level);
    }
    psychoJS.experiment.addData('key_checkInstr.keys', key_checkInstr.keys);
    psychoJS.experiment.addData('key_checkInstr.corr', key_checkInstr.corr);
    if (typeof key_checkInstr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_checkInstr.rt', key_checkInstr.rt);
        psychoJS.experiment.addData('key_checkInstr.duration', key_checkInstr.duration);
        routineTimer.reset();
        }
    
    key_checkInstr.stop();
    // Run 'End Routine' code from code_checkIntr
    if ((key_checkInstr.corr === 1)) {
        fbtext_checkInstr = "Correct! Press A key when the tip of T is facing left.";
    } else {
        fbtext_checkInstr = "Incorrect! Press A key when the tip of T is facing left.";
    }
    
    // the Routine "CheckInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_feedbackCheckInstr_allKeys;
var CheckInstr_FBComponents;
function CheckInstr_FBRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'CheckInstr_FB' ---
    t = 0;
    CheckInstr_FBClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('CheckInstr_FB.started', globalClock.getTime());
    feedback_CheckInstr1.setText(fbtext_checkInstr);
    key_feedbackCheckInstr.keys = undefined;
    key_feedbackCheckInstr.rt = undefined;
    _key_feedbackCheckInstr_allKeys = [];
    // keep track of which components have finished
    CheckInstr_FBComponents = [];
    CheckInstr_FBComponents.push(feedback_CheckInstr1);
    CheckInstr_FBComponents.push(feedback_CheckInstr2);
    CheckInstr_FBComponents.push(key_feedbackCheckInstr);
    
    for (const thisComponent of CheckInstr_FBComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function CheckInstr_FBRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'CheckInstr_FB' ---
    // get current time
    t = CheckInstr_FBClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_CheckInstr1* updates
    if (t >= 0.0 && feedback_CheckInstr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_CheckInstr1.tStart = t;  // (not accounting for frame time here)
      feedback_CheckInstr1.frameNStart = frameN;  // exact frame index
      
      feedback_CheckInstr1.setAutoDraw(true);
    }
    
    
    // *feedback_CheckInstr2* updates
    if (t >= 0.0 && feedback_CheckInstr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_CheckInstr2.tStart = t;  // (not accounting for frame time here)
      feedback_CheckInstr2.frameNStart = frameN;  // exact frame index
      
      feedback_CheckInstr2.setAutoDraw(true);
    }
    
    
    // *key_feedbackCheckInstr* updates
    if (t >= 0 && key_feedbackCheckInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_feedbackCheckInstr.tStart = t;  // (not accounting for frame time here)
      key_feedbackCheckInstr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_feedbackCheckInstr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_feedbackCheckInstr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_feedbackCheckInstr.clearEvents(); });
    }
    
    if (key_feedbackCheckInstr.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_feedbackCheckInstr.getKeys({keyList: ['space'], waitRelease: false});
      _key_feedbackCheckInstr_allKeys = _key_feedbackCheckInstr_allKeys.concat(theseKeys);
      if (_key_feedbackCheckInstr_allKeys.length > 0) {
        key_feedbackCheckInstr.keys = _key_feedbackCheckInstr_allKeys[_key_feedbackCheckInstr_allKeys.length - 1].name;  // just the last key pressed
        key_feedbackCheckInstr.rt = _key_feedbackCheckInstr_allKeys[_key_feedbackCheckInstr_allKeys.length - 1].rt;
        key_feedbackCheckInstr.duration = _key_feedbackCheckInstr_allKeys[_key_feedbackCheckInstr_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of CheckInstr_FBComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function CheckInstr_FBRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'CheckInstr_FB' ---
    for (const thisComponent of CheckInstr_FBComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('CheckInstr_FB.stopped', globalClock.getTime());
    key_feedbackCheckInstr.stop();
    // the Routine "CheckInstr_FB" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_InstrMainExp_allKeys;
var Instruction_MainExpComponents;
function Instruction_MainExpRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction_MainExp' ---
    t = 0;
    Instruction_MainExpClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instruction_MainExp.started', globalClock.getTime());
    key_InstrMainExp.keys = undefined;
    key_InstrMainExp.rt = undefined;
    _key_InstrMainExp_allKeys = [];
    // keep track of which components have finished
    Instruction_MainExpComponents = [];
    Instruction_MainExpComponents.push(InstrMainExp);
    Instruction_MainExpComponents.push(key_InstrMainExp);
    
    for (const thisComponent of Instruction_MainExpComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction_MainExpRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction_MainExp' ---
    // get current time
    t = Instruction_MainExpClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *InstrMainExp* updates
    if (t >= 0 && InstrMainExp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrMainExp.tStart = t;  // (not accounting for frame time here)
      InstrMainExp.frameNStart = frameN;  // exact frame index
      
      InstrMainExp.setAutoDraw(true);
    }
    
    
    // *key_InstrMainExp* updates
    if (t >= 1 && key_InstrMainExp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_InstrMainExp.tStart = t;  // (not accounting for frame time here)
      key_InstrMainExp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_InstrMainExp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_InstrMainExp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_InstrMainExp.clearEvents(); });
    }
    
    if (key_InstrMainExp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_InstrMainExp.getKeys({keyList: ['space'], waitRelease: false});
      _key_InstrMainExp_allKeys = _key_InstrMainExp_allKeys.concat(theseKeys);
      if (_key_InstrMainExp_allKeys.length > 0) {
        key_InstrMainExp.keys = _key_InstrMainExp_allKeys[_key_InstrMainExp_allKeys.length - 1].name;  // just the last key pressed
        key_InstrMainExp.rt = _key_InstrMainExp_allKeys[_key_InstrMainExp_allKeys.length - 1].rt;
        key_InstrMainExp.duration = _key_InstrMainExp_allKeys[_key_InstrMainExp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction_MainExpComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction_MainExpRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction_MainExp' ---
    for (const thisComponent of Instruction_MainExpComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instruction_MainExp.stopped', globalClock.getTime());
    key_InstrMainExp.stop();
    // the Routine "Instruction_MainExp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var remainingblock;
var breakTime;
var _key_respBreak_allKeys;
var TakeABreakComponents;
function TakeABreakRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TakeABreak' ---
    t = 0;
    TakeABreakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('TakeABreak.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_break
    remainingblock = (24 - block);
    breakTime = 16;
    if (((trial % breakTime) === 0)) {
        continueRoutine = true;
        sumcorr = (sumcorr + key_respMain.corr);
        sumrt = (sumrt + key_respMain.rt);
        avgcorr = (100 * (sumcorr / breakTime));
        avgrt = (sumrt / breakTime);
        if ((avgcorr > 90)) {
            accfbcolor = "green";
            accfbtext = (("Your accuracy during the last block was " + util.round(avgcorr, 2).toString()) + "%. Good job!");
        } else {
            accfbcolor = "red";
            accfbtext = (("Your accuracy during the last block was only " + util.round(avgcorr, 2).toString()) + "%. Please try to be accurate.");
        }
        if ((avgrt < 4.0)) {
            rtfbcolor = "green";
            rtfbtext = (("It took you an average of " + util.round(avgrt, 2).toString()) + "s to respond to the letter T. Good job!");
        } else {
            rtfbcolor = "red";
            rtfbtext = (("It took you an average of " + util.round(avgrt, 2).toString()) + "s to respond to the letter T. Please try to be faster.");
        }
        sumcorr = 0;
        sumrt = 0;
    } else {
        sumcorr = (sumcorr + key_respMain.corr);
        sumrt = (sumrt + key_respMain.rt);
        continueRoutine = false;
    }
    if ((remainingblock === 0)) {
        continueRoutine = false;
    }
    
    acctext.setColor(new util.Color(accfbcolor));
    acctext.setText(accfbtext);
    rttext.setColor(new util.Color(rtfbcolor));
    rttext.setText(rtfbtext);
    textBlockRemaining.setText(remainingblock);
    key_respBreak.keys = undefined;
    key_respBreak.rt = undefined;
    _key_respBreak_allKeys = [];
    // keep track of which components have finished
    TakeABreakComponents = [];
    TakeABreakComponents.push(acctext);
    TakeABreakComponents.push(rttext);
    TakeABreakComponents.push(textBreak);
    TakeABreakComponents.push(textBlockRemaining);
    TakeABreakComponents.push(key_respBreak);
    
    for (const thisComponent of TakeABreakComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TakeABreakRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TakeABreak' ---
    // get current time
    t = TakeABreakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *acctext* updates
    if (t >= 0.0 && acctext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      acctext.tStart = t;  // (not accounting for frame time here)
      acctext.frameNStart = frameN;  // exact frame index
      
      acctext.setAutoDraw(true);
    }
    
    
    // *rttext* updates
    if (t >= 0.0 && rttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rttext.tStart = t;  // (not accounting for frame time here)
      rttext.frameNStart = frameN;  // exact frame index
      
      rttext.setAutoDraw(true);
    }
    
    
    // *textBreak* updates
    if (t >= 0.0 && textBreak.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textBreak.tStart = t;  // (not accounting for frame time here)
      textBreak.frameNStart = frameN;  // exact frame index
      
      textBreak.setAutoDraw(true);
    }
    
    
    if (textBlockRemaining.status === PsychoJS.Status.STARTED){ // only update if being drawn
      textBlockRemaining.setPos([0, (- 65)], false);
    }
    
    // *textBlockRemaining* updates
    if (t >= 0.0 && textBlockRemaining.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textBlockRemaining.tStart = t;  // (not accounting for frame time here)
      textBlockRemaining.frameNStart = frameN;  // exact frame index
      
      textBlockRemaining.setAutoDraw(true);
    }
    
    
    // *key_respBreak* updates
    if (t >= 0.0 && key_respBreak.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respBreak.tStart = t;  // (not accounting for frame time here)
      key_respBreak.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respBreak.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respBreak.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respBreak.clearEvents(); });
    }
    
    if (key_respBreak.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respBreak.getKeys({keyList: ['space'], waitRelease: false});
      _key_respBreak_allKeys = _key_respBreak_allKeys.concat(theseKeys);
      if (_key_respBreak_allKeys.length > 0) {
        key_respBreak.keys = _key_respBreak_allKeys[_key_respBreak_allKeys.length - 1].name;  // just the last key pressed
        key_respBreak.rt = _key_respBreak_allKeys[_key_respBreak_allKeys.length - 1].rt;
        key_respBreak.duration = _key_respBreak_allKeys[_key_respBreak_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TakeABreakComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TakeABreakRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TakeABreak' ---
    for (const thisComponent of TakeABreakComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TakeABreak.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respBreak.corr, level);
    }
    psychoJS.experiment.addData('key_respBreak.keys', key_respBreak.keys);
    if (typeof key_respBreak.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respBreak.rt', key_respBreak.rt);
        psychoJS.experiment.addData('key_respBreak.duration', key_respBreak.duration);
        routineTimer.reset();
        }
    
    key_respBreak.stop();
    // the Routine "TakeABreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_respTesting_allKeys;
var displayTestingPhaseComponents;
function displayTestingPhaseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'displayTestingPhase' ---
    t = 0;
    displayTestingPhaseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('displayTestingPhase.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_initial_3
    psychoJS.window.mouseVisible = true;
    mouselocation = [0, 0];
    whichframe = 0;
    mouselocationlistx = [];
    mouselocationlisty = [];
    whichframelist = [];
    startApertureTime = 10000;
    lettersize = (28 * expInfo["ratio_monitor2CRT"]);
    aperturesize = (8000 * expInfo["ratio_monitor2CRT"]);
    searchsize = (482 * expInfo["ratio_monitor2CRT"]);
    newtlocx = (tlocx * expInfo["ratio_monitor2CRT"]);
    newtlocy = (tlocy * expInfo["ratio_monitor2CRT"]);
    newd1x = (d1x * expInfo["ratio_monitor2CRT"]);
    newd1y = (d1y * expInfo["ratio_monitor2CRT"]);
    newd2x = (d2x * expInfo["ratio_monitor2CRT"]);
    newd2y = (d2y * expInfo["ratio_monitor2CRT"]);
    newd3x = (d3x * expInfo["ratio_monitor2CRT"]);
    newd3y = (d3y * expInfo["ratio_monitor2CRT"]);
    newd4x = (d4x * expInfo["ratio_monitor2CRT"]);
    newd4y = (d4y * expInfo["ratio_monitor2CRT"]);
    newd5x = (d5x * expInfo["ratio_monitor2CRT"]);
    newd5y = (d5y * expInfo["ratio_monitor2CRT"]);
    newd6x = (d6x * expInfo["ratio_monitor2CRT"]);
    newd6y = (d6y * expInfo["ratio_monitor2CRT"]);
    newd7x = (d7x * expInfo["ratio_monitor2CRT"]);
    newd7y = (d7y * expInfo["ratio_monitor2CRT"]);
    newd8x = (d8x * expInfo["ratio_monitor2CRT"]);
    newd8y = (d8y * expInfo["ratio_monitor2CRT"]);
    newd9x = (d9x * expInfo["ratio_monitor2CRT"]);
    newd9y = (d9y * expInfo["ratio_monitor2CRT"]);
    newd10x = (d10x * expInfo["ratio_monitor2CRT"]);
    newd10y = (d10y * expInfo["ratio_monitor2CRT"]);
    newd11x = (d11x * expInfo["ratio_monitor2CRT"]);
    newd11y = (d11y * expInfo["ratio_monitor2CRT"]);
    hintlocation = (255 * expInfo["ratio_monitor2CRT"]);
    
    background_3.setSize([searchsize, searchsize]);
    imageT_3.setPos([newtlocx, newtlocy]);
    imageT_3.setSize([lettersize, lettersize]);
    imageT_3.setOri(targOrientdeg);
    imageL1_3.setPos([newd1x, newd1y]);
    imageL1_3.setSize([lettersize, lettersize]);
    imageL1_3.setOri(d1Orient);
    imageL2_3.setPos([newd2x, newd2y]);
    imageL2_3.setSize([lettersize, lettersize]);
    imageL2_3.setOri(d2Orient);
    imageL3_3.setPos([newd3x, newd3y]);
    imageL3_3.setSize([lettersize, lettersize]);
    imageL3_3.setOri(d3Orient);
    imageL4_3.setPos([newd4x, newd4y]);
    imageL4_3.setSize([lettersize, lettersize]);
    imageL4_3.setOri(d4Orient);
    imageL5_3.setPos([newd5x, newd5y]);
    imageL5_3.setSize([lettersize, lettersize]);
    imageL5_3.setOri(d5Orient);
    imageL6_3.setPos([newd6x, newd6y]);
    imageL6_3.setSize([lettersize, lettersize]);
    imageL6_3.setOri(d6Orient);
    imageL7_3.setPos([newd7x, newd7y]);
    imageL7_3.setSize([lettersize, lettersize]);
    imageL7_3.setOri(d7Orient);
    imageL8_3.setPos([newd8x, newd8y]);
    imageL8_3.setSize([lettersize, lettersize]);
    imageL8_3.setOri(d8Orient);
    imageL9_3.setPos([newd9x, newd9y]);
    imageL9_3.setSize([lettersize, lettersize]);
    imageL9_3.setOri(d9Orient);
    imageL10_3.setPos([newd10x, newd10y]);
    imageL10_3.setSize([lettersize, lettersize]);
    imageL10_3.setOri(d10Orient);
    imageL11_3.setPos([newd11x, newd11y]);
    imageL11_3.setSize([lettersize, lettersize]);
    imageL11_3.setOri(d11Orient);
    imageAperture_3.setSize([aperturesize, aperturesize]);
    CenterAperture_3.setPos([0, 0]);
    CenterAperture_3.setSize([aperturesize, aperturesize]);
    key_respTesting.keys = undefined;
    key_respTesting.rt = undefined;
    _key_respTesting_allKeys = [];
    // keep track of which components have finished
    displayTestingPhaseComponents = [];
    displayTestingPhaseComponents.push(background_3);
    displayTestingPhaseComponents.push(imageT_3);
    displayTestingPhaseComponents.push(imageL1_3);
    displayTestingPhaseComponents.push(imageL2_3);
    displayTestingPhaseComponents.push(imageL3_3);
    displayTestingPhaseComponents.push(imageL4_3);
    displayTestingPhaseComponents.push(imageL5_3);
    displayTestingPhaseComponents.push(imageL6_3);
    displayTestingPhaseComponents.push(imageL7_3);
    displayTestingPhaseComponents.push(imageL8_3);
    displayTestingPhaseComponents.push(imageL9_3);
    displayTestingPhaseComponents.push(imageL10_3);
    displayTestingPhaseComponents.push(imageL11_3);
    displayTestingPhaseComponents.push(imageAperture_3);
    displayTestingPhaseComponents.push(CenterAperture_3);
    displayTestingPhaseComponents.push(key_respTesting);
    
    for (const thisComponent of displayTestingPhaseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function displayTestingPhaseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'displayTestingPhase' ---
    // get current time
    t = displayTestingPhaseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_3* updates
    if (t >= 0.0 && background_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_3.tStart = t;  // (not accounting for frame time here)
      background_3.frameNStart = frameN;  // exact frame index
      
      background_3.setAutoDraw(true);
    }
    
    
    // *imageT_3* updates
    if (t >= 0 && imageT_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageT_3.tStart = t;  // (not accounting for frame time here)
      imageT_3.frameNStart = frameN;  // exact frame index
      
      imageT_3.setAutoDraw(true);
    }
    
    
    // *imageL1_3* updates
    if (t >= 0 && imageL1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL1_3.tStart = t;  // (not accounting for frame time here)
      imageL1_3.frameNStart = frameN;  // exact frame index
      
      imageL1_3.setAutoDraw(true);
    }
    
    
    // *imageL2_3* updates
    if (t >= 0 && imageL2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL2_3.tStart = t;  // (not accounting for frame time here)
      imageL2_3.frameNStart = frameN;  // exact frame index
      
      imageL2_3.setAutoDraw(true);
    }
    
    
    // *imageL3_3* updates
    if (t >= 0 && imageL3_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL3_3.tStart = t;  // (not accounting for frame time here)
      imageL3_3.frameNStart = frameN;  // exact frame index
      
      imageL3_3.setAutoDraw(true);
    }
    
    
    // *imageL4_3* updates
    if (t >= 0 && imageL4_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL4_3.tStart = t;  // (not accounting for frame time here)
      imageL4_3.frameNStart = frameN;  // exact frame index
      
      imageL4_3.setAutoDraw(true);
    }
    
    
    // *imageL5_3* updates
    if (t >= 0 && imageL5_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL5_3.tStart = t;  // (not accounting for frame time here)
      imageL5_3.frameNStart = frameN;  // exact frame index
      
      imageL5_3.setAutoDraw(true);
    }
    
    
    // *imageL6_3* updates
    if (t >= 0 && imageL6_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL6_3.tStart = t;  // (not accounting for frame time here)
      imageL6_3.frameNStart = frameN;  // exact frame index
      
      imageL6_3.setAutoDraw(true);
    }
    
    
    // *imageL7_3* updates
    if (t >= 0 && imageL7_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL7_3.tStart = t;  // (not accounting for frame time here)
      imageL7_3.frameNStart = frameN;  // exact frame index
      
      imageL7_3.setAutoDraw(true);
    }
    
    
    // *imageL8_3* updates
    if (t >= 0 && imageL8_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL8_3.tStart = t;  // (not accounting for frame time here)
      imageL8_3.frameNStart = frameN;  // exact frame index
      
      imageL8_3.setAutoDraw(true);
    }
    
    
    // *imageL9_3* updates
    if (t >= 0 && imageL9_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL9_3.tStart = t;  // (not accounting for frame time here)
      imageL9_3.frameNStart = frameN;  // exact frame index
      
      imageL9_3.setAutoDraw(true);
    }
    
    
    // *imageL10_3* updates
    if (t >= 0 && imageL10_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL10_3.tStart = t;  // (not accounting for frame time here)
      imageL10_3.frameNStart = frameN;  // exact frame index
      
      imageL10_3.setAutoDraw(true);
    }
    
    
    // *imageL11_3* updates
    if (t >= 0 && imageL11_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL11_3.tStart = t;  // (not accounting for frame time here)
      imageL11_3.frameNStart = frameN;  // exact frame index
      
      imageL11_3.setAutoDraw(true);
    }
    
    
    if (imageAperture_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      imageAperture_3.setPos(mouselocation, false);
    }
    
    // *imageAperture_3* updates
    if (t >= startApertureTime && imageAperture_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageAperture_3.tStart = t;  // (not accounting for frame time here)
      imageAperture_3.frameNStart = frameN;  // exact frame index
      
      imageAperture_3.setAutoDraw(true);
    }
    
    
    // *CenterAperture_3* updates
    if (t >= startApertureTime && CenterAperture_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CenterAperture_3.tStart = t;  // (not accounting for frame time here)
      CenterAperture_3.frameNStart = frameN;  // exact frame index
      
      CenterAperture_3.setAutoDraw(true);
    }
    
    if (CenterAperture_3.status === PsychoJS.Status.STARTED && frameN >= (CenterAperture_3.frameNStart + 1)) {
      CenterAperture_3.setAutoDraw(false);
    }
    
    // *key_respTesting* updates
    if (t >= 0 && key_respTesting.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respTesting.tStart = t;  // (not accounting for frame time here)
      key_respTesting.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respTesting.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respTesting.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respTesting.clearEvents(); });
    }
    
    if (key_respTesting.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respTesting.getKeys({keyList: ['a', 's'], waitRelease: false});
      _key_respTesting_allKeys = _key_respTesting_allKeys.concat(theseKeys);
      if (_key_respTesting_allKeys.length > 0) {
        key_respTesting.keys = _key_respTesting_allKeys[0].name;  // just the first key pressed
        key_respTesting.rt = _key_respTesting_allKeys[0].rt;
        key_respTesting.duration = _key_respTesting_allKeys[0].duration;
        // was this correct?
        if (key_respTesting.keys == corrAnswer) {
            key_respTesting.corr = 1;
        } else {
            key_respTesting.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of displayTestingPhaseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function displayTestingPhaseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'displayTestingPhase' ---
    for (const thisComponent of displayTestingPhaseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('displayTestingPhase.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_initial_3
    psychoJS.experiment.addData("letterSize", lettersize);
    psychoJS.experiment.addData("apertureSize", aperturesize);
    psychoJS.experiment.addData("searchsize", searchsize);
    
    // was no response the correct answer?!
    if (key_respTesting.keys === undefined) {
      if (['None','none',undefined].includes(corrAnswer)) {
         key_respTesting.corr = 1;  // correct non-response
      } else {
         key_respTesting.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respTesting.corr, level);
    }
    psychoJS.experiment.addData('key_respTesting.keys', key_respTesting.keys);
    psychoJS.experiment.addData('key_respTesting.corr', key_respTesting.corr);
    if (typeof key_respTesting.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respTesting.rt', key_respTesting.rt);
        psychoJS.experiment.addData('key_respTesting.duration', key_respTesting.duration);
        routineTimer.reset();
        }
    
    key_respTesting.stop();
    // Run 'End Routine' code from code_ending
    mouselocation = [0, 0];
    if ((key_respTesting.corr === 1)) {
        fbtext = "correct!";
        fbcolor = "green";
        fbdur = 0.2;
    } else {
        fbtext = "incorrect!";
        fbcolor = "red";
        fbdur = 4;
    }
    
    // the Routine "displayTestingPhase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_RespBreak_allKeys;
var TakeABreak2Components;
function TakeABreak2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TakeABreak2' ---
    t = 0;
    TakeABreak2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('TakeABreak2.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_break2
    remainingblock = (4 - block);
    breakTime = 16;
    if (((trial % breakTime) === 0)) {
        continueRoutine = true;
        sumcorr = (sumcorr + key_respTesting.corr);
        sumrt = (sumrt + key_respTesting.rt);
        avgcorr = (100 * (sumcorr / breakTime));
        avgrt = (sumrt / breakTime);
        if ((avgcorr > 90)) {
            accfbcolor = "green";
            accfbtext = (("Your accuracy during the last block was " + util.round(avgcorr, 2).toString()) + "%. Good job!");
        } else {
            accfbcolor = "red";
            accfbtext = (("Your accuracy during the last block was only " + util.round(avgcorr, 2).toString()) + "%. Please try to be accurate.");
        }
        if ((avgrt < 4.0)) {
            rtfbcolor = "green";
            rtfbtext = (("It took you an average of " + util.round(avgrt, 2).toString()) + "s to respond to the letter T. Good job!");
        } else {
            rtfbcolor = "red";
            rtfbtext = (("It took you an average of " + util.round(avgrt, 2).toString()) + "s to respond to the letter T. Please try to be faster.");
        }
        sumcorr = 0;
        sumrt = 0;
    } else {
        sumcorr = (sumcorr + key_respTesting.corr);
        sumrt = (sumrt + key_respTesting.rt);
        continueRoutine = false;
    }
    if ((remainingblock === 0)) {
        continueRoutine = false;
    }
    
    accText.setText(accfbtext);
    rtText.setText(rtfbtext);
    textblockRemaining.setText(remainingblock);
    key_RespBreak.keys = undefined;
    key_RespBreak.rt = undefined;
    _key_RespBreak_allKeys = [];
    // keep track of which components have finished
    TakeABreak2Components = [];
    TakeABreak2Components.push(accText);
    TakeABreak2Components.push(rtText);
    TakeABreak2Components.push(TextBreak);
    TakeABreak2Components.push(textblockRemaining);
    TakeABreak2Components.push(key_RespBreak);
    
    for (const thisComponent of TakeABreak2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TakeABreak2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TakeABreak2' ---
    // get current time
    t = TakeABreak2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *accText* updates
    if (t >= 0.0 && accText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      accText.tStart = t;  // (not accounting for frame time here)
      accText.frameNStart = frameN;  // exact frame index
      
      accText.setAutoDraw(true);
    }
    
    
    // *rtText* updates
    if (t >= 0.0 && rtText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rtText.tStart = t;  // (not accounting for frame time here)
      rtText.frameNStart = frameN;  // exact frame index
      
      rtText.setAutoDraw(true);
    }
    
    
    // *TextBreak* updates
    if (t >= 0.0 && TextBreak.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TextBreak.tStart = t;  // (not accounting for frame time here)
      TextBreak.frameNStart = frameN;  // exact frame index
      
      TextBreak.setAutoDraw(true);
    }
    
    
    if (textblockRemaining.status === PsychoJS.Status.STARTED){ // only update if being drawn
      textblockRemaining.setPos([0, (- 65)], false);
    }
    
    // *textblockRemaining* updates
    if (t >= 0.0 && textblockRemaining.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textblockRemaining.tStart = t;  // (not accounting for frame time here)
      textblockRemaining.frameNStart = frameN;  // exact frame index
      
      textblockRemaining.setAutoDraw(true);
    }
    
    
    // *key_RespBreak* updates
    if (t >= 0.0 && key_RespBreak.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_RespBreak.tStart = t;  // (not accounting for frame time here)
      key_RespBreak.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_RespBreak.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_RespBreak.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_RespBreak.clearEvents(); });
    }
    
    if (key_RespBreak.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_RespBreak.getKeys({keyList: ['space'], waitRelease: false});
      _key_RespBreak_allKeys = _key_RespBreak_allKeys.concat(theseKeys);
      if (_key_RespBreak_allKeys.length > 0) {
        key_RespBreak.keys = _key_RespBreak_allKeys[_key_RespBreak_allKeys.length - 1].name;  // just the last key pressed
        key_RespBreak.rt = _key_RespBreak_allKeys[_key_RespBreak_allKeys.length - 1].rt;
        key_RespBreak.duration = _key_RespBreak_allKeys[_key_RespBreak_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TakeABreak2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TakeABreak2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TakeABreak2' ---
    for (const thisComponent of TakeABreak2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TakeABreak2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_RespBreak.corr, level);
    }
    psychoJS.experiment.addData('key_RespBreak.keys', key_RespBreak.keys);
    if (typeof key_RespBreak.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_RespBreak.rt', key_RespBreak.rt);
        psychoJS.experiment.addData('key_RespBreak.duration', key_RespBreak.duration);
        routineTimer.reset();
        }
    
    key_RespBreak.stop();
    // the Routine "TakeABreak2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_AnswerQues_allKeys;
var RecogQuestionComponents;
function RecogQuestionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RecogQuestion' ---
    t = 0;
    RecogQuestionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('RecogQuestion.started', globalClock.getTime());
    key_AnswerQues.keys = undefined;
    key_AnswerQues.rt = undefined;
    _key_AnswerQues_allKeys = [];
    // keep track of which components have finished
    RecogQuestionComponents = [];
    RecogQuestionComponents.push(Ques_text);
    RecogQuestionComponents.push(key_AnswerQues);
    
    for (const thisComponent of RecogQuestionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RecogQuestionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RecogQuestion' ---
    // get current time
    t = RecogQuestionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Ques_text* updates
    if (t >= 0 && Ques_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Ques_text.tStart = t;  // (not accounting for frame time here)
      Ques_text.frameNStart = frameN;  // exact frame index
      
      Ques_text.setAutoDraw(true);
    }
    
    
    // *key_AnswerQues* updates
    if (t >= 1 && key_AnswerQues.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_AnswerQues.tStart = t;  // (not accounting for frame time here)
      key_AnswerQues.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_AnswerQues.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_AnswerQues.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_AnswerQues.clearEvents(); });
    }
    
    if (key_AnswerQues.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_AnswerQues.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_AnswerQues_allKeys = _key_AnswerQues_allKeys.concat(theseKeys);
      if (_key_AnswerQues_allKeys.length > 0) {
        key_AnswerQues.keys = _key_AnswerQues_allKeys[0].name;  // just the first key pressed
        key_AnswerQues.rt = _key_AnswerQues_allKeys[0].rt;
        key_AnswerQues.duration = _key_AnswerQues_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RecogQuestionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RecogQuestionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RecogQuestion' ---
    for (const thisComponent of RecogQuestionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RecogQuestion.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_AnswerQues.corr, level);
    }
    psychoJS.experiment.addData('key_AnswerQues.keys', key_AnswerQues.keys);
    if (typeof key_AnswerQues.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_AnswerQues.rt', key_AnswerQues.rt);
        psychoJS.experiment.addData('key_AnswerQues.duration', key_AnswerQues.duration);
        routineTimer.reset();
        }
    
    key_AnswerQues.stop();
    // the Routine "RecogQuestion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _continue_key_allKeys;
var DiscloseComponents;
function DiscloseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Disclose' ---
    t = 0;
    DiscloseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Disclose.started', globalClock.getTime());
    continue_key.keys = undefined;
    continue_key.rt = undefined;
    _continue_key_allKeys = [];
    // keep track of which components have finished
    DiscloseComponents = [];
    DiscloseComponents.push(Disclose_text);
    DiscloseComponents.push(continue_key);
    
    for (const thisComponent of DiscloseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function DiscloseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Disclose' ---
    // get current time
    t = DiscloseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Disclose_text* updates
    if (t >= 0.0 && Disclose_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Disclose_text.tStart = t;  // (not accounting for frame time here)
      Disclose_text.frameNStart = frameN;  // exact frame index
      
      Disclose_text.setAutoDraw(true);
    }
    
    
    // *continue_key* updates
    if (t >= 1 && continue_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_key.tStart = t;  // (not accounting for frame time here)
      continue_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { continue_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { continue_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { continue_key.clearEvents(); });
    }
    
    if (continue_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = continue_key.getKeys({keyList: ['space'], waitRelease: false});
      _continue_key_allKeys = _continue_key_allKeys.concat(theseKeys);
      if (_continue_key_allKeys.length > 0) {
        continue_key.keys = _continue_key_allKeys[_continue_key_allKeys.length - 1].name;  // just the last key pressed
        continue_key.rt = _continue_key_allKeys[_continue_key_allKeys.length - 1].rt;
        continue_key.duration = _continue_key_allKeys[_continue_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of DiscloseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function DiscloseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Disclose' ---
    for (const thisComponent of DiscloseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Disclose.stopped', globalClock.getTime());
    continue_key.stop();
    // the Routine "Disclose" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _InstrRecognitionTest_key_allKeys;
var InstrRTComponents;
function InstrRTRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'InstrRT' ---
    t = 0;
    InstrRTClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('InstrRT.started', globalClock.getTime());
    InstrRecognitionTest_key.keys = undefined;
    InstrRecognitionTest_key.rt = undefined;
    _InstrRecognitionTest_key_allKeys = [];
    // keep track of which components have finished
    InstrRTComponents = [];
    InstrRTComponents.push(InstrRecognitionTest);
    InstrRTComponents.push(InstrRecognitionTest_key);
    
    for (const thisComponent of InstrRTComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstrRTRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstrRT' ---
    // get current time
    t = InstrRTClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *InstrRecognitionTest* updates
    if (t >= 0.0 && InstrRecognitionTest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrRecognitionTest.tStart = t;  // (not accounting for frame time here)
      InstrRecognitionTest.frameNStart = frameN;  // exact frame index
      
      InstrRecognitionTest.setAutoDraw(true);
    }
    
    
    // *InstrRecognitionTest_key* updates
    if (t >= 1 && InstrRecognitionTest_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrRecognitionTest_key.tStart = t;  // (not accounting for frame time here)
      InstrRecognitionTest_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { InstrRecognitionTest_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { InstrRecognitionTest_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { InstrRecognitionTest_key.clearEvents(); });
    }
    
    if (InstrRecognitionTest_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = InstrRecognitionTest_key.getKeys({keyList: ['space'], waitRelease: false});
      _InstrRecognitionTest_key_allKeys = _InstrRecognitionTest_key_allKeys.concat(theseKeys);
      if (_InstrRecognitionTest_key_allKeys.length > 0) {
        InstrRecognitionTest_key.keys = _InstrRecognitionTest_key_allKeys[_InstrRecognitionTest_key_allKeys.length - 1].name;  // just the last key pressed
        InstrRecognitionTest_key.rt = _InstrRecognitionTest_key_allKeys[_InstrRecognitionTest_key_allKeys.length - 1].rt;
        InstrRecognitionTest_key.duration = _InstrRecognitionTest_key_allKeys[_InstrRecognitionTest_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstrRTComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstrRTRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstrRT' ---
    for (const thisComponent of InstrRTComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('InstrRT.stopped', globalClock.getTime());
    InstrRecognitionTest_key.stop();
    // the Routine "InstrRT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fixation_RTComponents;
function fixation_RTRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation_RT' ---
    t = 0;
    fixation_RTClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation_RT.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_RTfix
    psychoJS.window.mouseVisible = true;
    if ((phase === "rt")) {
        fixationStartTime = 0;
    } else {
        fixationStartTime = 0;
    }
    psychoJS.window.mouseVisible = true;
    fixsize = (28 * expInfo["ratio_monitor2CRT"]);
    hintlocation = (255 * expInfo["ratio_monitor2CRT"]);
    
    fixation_image.setSize([fixsize, fixsize]);
    fixationHint_text.setPos([0, hintlocation]);
    // setup some python lists for storing info about the mouseInitial
    // current position of the mouse:
    mouseInitial.x = [];
    mouseInitial.y = [];
    mouseInitial.leftButton = [];
    mouseInitial.midButton = [];
    mouseInitial.rightButton = [];
    mouseInitial.time = [];
    mouseInitial.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouseInitial.mouseClock.reset();
    // keep track of which components have finished
    fixation_RTComponents = [];
    fixation_RTComponents.push(fixation_image);
    fixation_RTComponents.push(fixationHint_text);
    fixation_RTComponents.push(mouseInitial);
    
    for (const thisComponent of fixation_RTComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fixation_RTRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation_RT' ---
    // get current time
    t = fixation_RTClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_image* updates
    if (t >= 0.0 && fixation_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_image.tStart = t;  // (not accounting for frame time here)
      fixation_image.frameNStart = frameN;  // exact frame index
      
      fixation_image.setAutoDraw(true);
    }
    
    
    // *fixationHint_text* updates
    if (t >= fixationStartTime && fixationHint_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationHint_text.tStart = t;  // (not accounting for frame time here)
      fixationHint_text.frameNStart = frameN;  // exact frame index
      
      fixationHint_text.setAutoDraw(true);
    }
    
    // *mouseInitial* updates
    if (t >= 0.0 && mouseInitial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseInitial.tStart = t;  // (not accounting for frame time here)
      mouseInitial.frameNStart = frameN;  // exact frame index
      
      mouseInitial.status = PsychoJS.Status.STARTED;
      prevButtonState = mouseInitial.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseInitial.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseInitial.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [fixationPoint]) {
            if (obj.contains(mouseInitial)) {
              gotValidClick = true;
              mouseInitial.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouseInitial.getPos();
          mouseInitial.x.push(_mouseXYs[0]);
          mouseInitial.y.push(_mouseXYs[1]);
          mouseInitial.leftButton.push(_mouseButtons[0]);
          mouseInitial.midButton.push(_mouseButtons[1]);
          mouseInitial.rightButton.push(_mouseButtons[2]);
          mouseInitial.time.push(mouseInitial.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixation_RTComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation_RTRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation_RT' ---
    for (const thisComponent of fixation_RTComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fixation_RT.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_RTfix
    mouselocation = [0, 0];
    psychoJS.experiment.addData("fixationSize", fixsize);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouseInitial.x) {  psychoJS.experiment.addData('mouseInitial.x', mouseInitial.x[0])};
    if (mouseInitial.y) {  psychoJS.experiment.addData('mouseInitial.y', mouseInitial.y[0])};
    if (mouseInitial.leftButton) {  psychoJS.experiment.addData('mouseInitial.leftButton', mouseInitial.leftButton[0])};
    if (mouseInitial.midButton) {  psychoJS.experiment.addData('mouseInitial.midButton', mouseInitial.midButton[0])};
    if (mouseInitial.rightButton) {  psychoJS.experiment.addData('mouseInitial.rightButton', mouseInitial.rightButton[0])};
    if (mouseInitial.time) {  psychoJS.experiment.addData('mouseInitial.time', mouseInitial.time[0])};
    if (mouseInitial.clicked_name) {  psychoJS.experiment.addData('mouseInitial.clicked_name', mouseInitial.clicked_name[0])};
    
    // the Routine "fixation_RT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_respRT_allKeys;
var displayRTComponents;
function displayRTRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'displayRT' ---
    t = 0;
    displayRTClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('displayRT.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_initial_2
    psychoJS.window.mouseVisible = true;
    mouselocation = [0, 0];
    whichframe = 0;
    mouselocationlistx = [];
    mouselocationlisty = [];
    whichframelist = [];
    startApertureTime = 10000;
    if ((phase === "rt")) {
        searchHintStartTime = 0;
        if ((block === 0)) {
            searchHintText = "Indicate whether you have seen it by Y or N";
        } else {
            searchHintText = "Indicate whether you have seen it by Y or N";
        }
    } else {
        searchHintStartTime = 10000;
    }
    lettersize = (28 * expInfo["ratio_monitor2CRT"]);
    aperturesize = (8000 * expInfo["ratio_monitor2CRT"]);
    searchsize = (482 * expInfo["ratio_monitor2CRT"]);
    newtlocx = (tlocx * expInfo["ratio_monitor2CRT"]);
    newtlocy = (tlocy * expInfo["ratio_monitor2CRT"]);
    newd1x = (d1x * expInfo["ratio_monitor2CRT"]);
    newd1y = (d1y * expInfo["ratio_monitor2CRT"]);
    newd2x = (d2x * expInfo["ratio_monitor2CRT"]);
    newd2y = (d2y * expInfo["ratio_monitor2CRT"]);
    newd3x = (d3x * expInfo["ratio_monitor2CRT"]);
    newd3y = (d3y * expInfo["ratio_monitor2CRT"]);
    newd4x = (d4x * expInfo["ratio_monitor2CRT"]);
    newd4y = (d4y * expInfo["ratio_monitor2CRT"]);
    newd5x = (d5x * expInfo["ratio_monitor2CRT"]);
    newd5y = (d5y * expInfo["ratio_monitor2CRT"]);
    newd6x = (d6x * expInfo["ratio_monitor2CRT"]);
    newd6y = (d6y * expInfo["ratio_monitor2CRT"]);
    newd7x = (d7x * expInfo["ratio_monitor2CRT"]);
    newd7y = (d7y * expInfo["ratio_monitor2CRT"]);
    newd8x = (d8x * expInfo["ratio_monitor2CRT"]);
    newd8y = (d8y * expInfo["ratio_monitor2CRT"]);
    newd9x = (d9x * expInfo["ratio_monitor2CRT"]);
    newd9y = (d9y * expInfo["ratio_monitor2CRT"]);
    newd10x = (d10x * expInfo["ratio_monitor2CRT"]);
    newd10y = (d10y * expInfo["ratio_monitor2CRT"]);
    newd11x = (d11x * expInfo["ratio_monitor2CRT"]);
    newd11y = (d11y * expInfo["ratio_monitor2CRT"]);
    hintlocation = (255 * expInfo["ratio_monitor2CRT"]);
    
    background_2.setSize([searchsize, searchsize]);
    imageT_2.setPos([newtlocx, newtlocy]);
    imageT_2.setSize([lettersize, lettersize]);
    imageT_2.setOri(targOrientdeg);
    imageL1_2.setPos([newd1x, newd1y]);
    imageL1_2.setSize([lettersize, lettersize]);
    imageL1_2.setOri(d1Orient);
    imageL2_2.setPos([newd2x, newd2y]);
    imageL2_2.setSize([lettersize, lettersize]);
    imageL2_2.setOri(d2Orient);
    imageL3_2.setPos([newd3x, newd3y]);
    imageL3_2.setSize([lettersize, lettersize]);
    imageL3_2.setOri(d3Orient);
    imageL4_2.setPos([newd4x, newd4y]);
    imageL4_2.setSize([lettersize, lettersize]);
    imageL4_2.setOri(d4Orient);
    imageL5_2.setPos([newd5x, newd5y]);
    imageL5_2.setSize([lettersize, lettersize]);
    imageL5_2.setOri(d5Orient);
    imageL6_2.setPos([newd6x, newd6y]);
    imageL6_2.setSize([lettersize, lettersize]);
    imageL6_2.setOri(d6Orient);
    imageL7_2.setPos([newd7x, newd7y]);
    imageL7_2.setSize([lettersize, lettersize]);
    imageL7_2.setOri(d7Orient);
    imageL8_2.setPos([newd8x, newd8y]);
    imageL8_2.setSize([lettersize, lettersize]);
    imageL8_2.setOri(d8Orient);
    imageL9_2.setPos([newd9x, newd9y]);
    imageL9_2.setSize([lettersize, lettersize]);
    imageL9_2.setOri(d9Orient);
    imageL10_2.setPos([newd10x, newd10y]);
    imageL10_2.setSize([lettersize, lettersize]);
    imageL10_2.setOri(d10Orient);
    imageL11_2.setPos([newd11x, newd11y]);
    imageL11_2.setSize([lettersize, lettersize]);
    imageL11_2.setOri(d11Orient);
    imageAperture_2.setSize([aperturesize, aperturesize]);
    CenterAperture_2.setPos([0, 0]);
    CenterAperture_2.setSize([aperturesize, aperturesize]);
    key_respRT.keys = undefined;
    key_respRT.rt = undefined;
    _key_respRT_allKeys = [];
    adjustHint_text.setPos([0, hintlocation]);
    adjustHint_text.setText(searchHintText);
    // keep track of which components have finished
    displayRTComponents = [];
    displayRTComponents.push(background_2);
    displayRTComponents.push(imageT_2);
    displayRTComponents.push(imageL1_2);
    displayRTComponents.push(imageL2_2);
    displayRTComponents.push(imageL3_2);
    displayRTComponents.push(imageL4_2);
    displayRTComponents.push(imageL5_2);
    displayRTComponents.push(imageL6_2);
    displayRTComponents.push(imageL7_2);
    displayRTComponents.push(imageL8_2);
    displayRTComponents.push(imageL9_2);
    displayRTComponents.push(imageL10_2);
    displayRTComponents.push(imageL11_2);
    displayRTComponents.push(imageAperture_2);
    displayRTComponents.push(CenterAperture_2);
    displayRTComponents.push(key_respRT);
    displayRTComponents.push(adjustHint_text);
    
    for (const thisComponent of displayRTComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function displayRTRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'displayRT' ---
    // get current time
    t = displayRTClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_2* updates
    if (t >= 0.0 && background_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_2.tStart = t;  // (not accounting for frame time here)
      background_2.frameNStart = frameN;  // exact frame index
      
      background_2.setAutoDraw(true);
    }
    
    
    // *imageT_2* updates
    if (t >= 0 && imageT_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageT_2.tStart = t;  // (not accounting for frame time here)
      imageT_2.frameNStart = frameN;  // exact frame index
      
      imageT_2.setAutoDraw(true);
    }
    
    
    // *imageL1_2* updates
    if (t >= 0 && imageL1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL1_2.tStart = t;  // (not accounting for frame time here)
      imageL1_2.frameNStart = frameN;  // exact frame index
      
      imageL1_2.setAutoDraw(true);
    }
    
    
    // *imageL2_2* updates
    if (t >= 0 && imageL2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL2_2.tStart = t;  // (not accounting for frame time here)
      imageL2_2.frameNStart = frameN;  // exact frame index
      
      imageL2_2.setAutoDraw(true);
    }
    
    
    // *imageL3_2* updates
    if (t >= 0 && imageL3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL3_2.tStart = t;  // (not accounting for frame time here)
      imageL3_2.frameNStart = frameN;  // exact frame index
      
      imageL3_2.setAutoDraw(true);
    }
    
    
    // *imageL4_2* updates
    if (t >= 0 && imageL4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL4_2.tStart = t;  // (not accounting for frame time here)
      imageL4_2.frameNStart = frameN;  // exact frame index
      
      imageL4_2.setAutoDraw(true);
    }
    
    
    // *imageL5_2* updates
    if (t >= 0 && imageL5_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL5_2.tStart = t;  // (not accounting for frame time here)
      imageL5_2.frameNStart = frameN;  // exact frame index
      
      imageL5_2.setAutoDraw(true);
    }
    
    
    // *imageL6_2* updates
    if (t >= 0 && imageL6_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL6_2.tStart = t;  // (not accounting for frame time here)
      imageL6_2.frameNStart = frameN;  // exact frame index
      
      imageL6_2.setAutoDraw(true);
    }
    
    
    // *imageL7_2* updates
    if (t >= 0 && imageL7_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL7_2.tStart = t;  // (not accounting for frame time here)
      imageL7_2.frameNStart = frameN;  // exact frame index
      
      imageL7_2.setAutoDraw(true);
    }
    
    
    // *imageL8_2* updates
    if (t >= 0 && imageL8_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL8_2.tStart = t;  // (not accounting for frame time here)
      imageL8_2.frameNStart = frameN;  // exact frame index
      
      imageL8_2.setAutoDraw(true);
    }
    
    
    // *imageL9_2* updates
    if (t >= 0 && imageL9_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL9_2.tStart = t;  // (not accounting for frame time here)
      imageL9_2.frameNStart = frameN;  // exact frame index
      
      imageL9_2.setAutoDraw(true);
    }
    
    
    // *imageL10_2* updates
    if (t >= 0 && imageL10_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL10_2.tStart = t;  // (not accounting for frame time here)
      imageL10_2.frameNStart = frameN;  // exact frame index
      
      imageL10_2.setAutoDraw(true);
    }
    
    
    // *imageL11_2* updates
    if (t >= 0 && imageL11_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageL11_2.tStart = t;  // (not accounting for frame time here)
      imageL11_2.frameNStart = frameN;  // exact frame index
      
      imageL11_2.setAutoDraw(true);
    }
    
    
    if (imageAperture_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      imageAperture_2.setPos(mouselocation, false);
    }
    
    // *imageAperture_2* updates
    if (t >= startApertureTime && imageAperture_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageAperture_2.tStart = t;  // (not accounting for frame time here)
      imageAperture_2.frameNStart = frameN;  // exact frame index
      
      imageAperture_2.setAutoDraw(true);
    }
    
    
    // *CenterAperture_2* updates
    if (t >= startApertureTime && CenterAperture_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CenterAperture_2.tStart = t;  // (not accounting for frame time here)
      CenterAperture_2.frameNStart = frameN;  // exact frame index
      
      CenterAperture_2.setAutoDraw(true);
    }
    
    if (CenterAperture_2.status === PsychoJS.Status.STARTED && frameN >= (CenterAperture_2.frameNStart + 1)) {
      CenterAperture_2.setAutoDraw(false);
    }
    
    // *key_respRT* updates
    if (t >= 0 && key_respRT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respRT.tStart = t;  // (not accounting for frame time here)
      key_respRT.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respRT.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respRT.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respRT.clearEvents(); });
    }
    
    if (key_respRT.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respRT.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_respRT_allKeys = _key_respRT_allKeys.concat(theseKeys);
      if (_key_respRT_allKeys.length > 0) {
        key_respRT.keys = _key_respRT_allKeys[0].name;  // just the first key pressed
        key_respRT.rt = _key_respRT_allKeys[0].rt;
        key_respRT.duration = _key_respRT_allKeys[0].duration;
        // was this correct?
        if (key_respRT.keys == corrAnswer) {
            key_respRT.corr = 1;
        } else {
            key_respRT.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *adjustHint_text* updates
    if (t >= searchHintStartTime && adjustHint_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      adjustHint_text.tStart = t;  // (not accounting for frame time here)
      adjustHint_text.frameNStart = frameN;  // exact frame index
      
      adjustHint_text.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of displayRTComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function displayRTRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'displayRT' ---
    for (const thisComponent of displayRTComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('displayRT.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_initial_2
    psychoJS.experiment.addData("letterSize", lettersize);
    psychoJS.experiment.addData("apertureSize", aperturesize);
    psychoJS.experiment.addData("searchsize", searchsize);
    
    // was no response the correct answer?!
    if (key_respRT.keys === undefined) {
      if (['None','none',undefined].includes(corrAnswer)) {
         key_respRT.corr = 1;  // correct non-response
      } else {
         key_respRT.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respRT.corr, level);
    }
    psychoJS.experiment.addData('key_respRT.keys', key_respRT.keys);
    psychoJS.experiment.addData('key_respRT.corr', key_respRT.corr);
    if (typeof key_respRT.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respRT.rt', key_respRT.rt);
        psychoJS.experiment.addData('key_respRT.duration', key_respRT.duration);
        routineTimer.reset();
        }
    
    key_respRT.stop();
    // the Routine "displayRT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EndOfExperimentComponents;
function EndOfExperimentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndOfExperiment' ---
    t = 0;
    EndOfExperimentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('EndOfExperiment.started', globalClock.getTime());
    // keep track of which components have finished
    EndOfExperimentComponents = [];
    EndOfExperimentComponents.push(textEnd);
    
    for (const thisComponent of EndOfExperimentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndOfExperimentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndOfExperiment' ---
    // get current time
    t = EndOfExperimentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textEnd* updates
    if (t >= 0.0 && textEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEnd.tStart = t;  // (not accounting for frame time here)
      textEnd.frameNStart = frameN;  // exact frame index
      
      textEnd.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textEnd.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textEnd.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndOfExperimentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndOfExperimentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndOfExperiment' ---
    for (const thisComponent of EndOfExperimentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EndOfExperiment.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
