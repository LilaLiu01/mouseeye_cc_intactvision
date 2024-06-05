#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.2),
    on Wed Nov  1 04:22:36 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.2.2')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.2'
expName = 'MouseEye_CC'  # from the Builder filename that created this script
expInfo = {
    'participant': '999',
    'designid': '12',
    'prolificid': 'xxx',
    'Gender': 'F',
    'Age': '18',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/seanliu/Documents/AMC_Lab/MouseEye/MouseEye_Prolific_ContextualCueing_fromscratch/MouseEye_CC.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.DEBUG)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1470, 956], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0, 0, 0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "InstrStartPage" ---
    # Run 'Begin Experiment' code from StartPage_code
    # Age Restrictions
    if (int(expInfo['Age']) < 18 or int(expInfo['Age']) > 45):
        core.quit()
    
    # design (rich quadrant)
    design = int(expInfo['designid']);
    parameterfile = 'MouseEyeCC_Seq'+str(design)+'.xlsx';
    testingfile = 'Testing_Seq'+str(design)+'.xlsx';
    rtfile = 'RT_Seq'+str(design)+'.xlsx';
    # participant monitor vs. CRT ratio = 1
    expInfo['ratio_monitor2CRT'] = 1;
    InstrStartPage_text = visual.TextStim(win=win, name='InstrStartPage_text',
        text='Welcome to our study! \n\nThis study requires about 20 minutes of uninterrupted time. Please choose a comfortable pose and try to keep the same pose during experiment. \n\nWe will first find out your monitor size, how far away you are sitting. Then you will do a visual search task.\n\nPress the spacebar to start when you are ready.\n',
        font='Arial',
        pos=(0, 0), height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-1.0);
    InstrStartPage_key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "VirtualChinrest" ---
    loading = visual.TextStim(win=win, name='loading',
        text='Loading......',
        font='Arial',
        pos=(0, 0), height=24, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "InstrRedo" ---
    InstrRedo_txt = visual.TextStim(win=win, name='InstrRedo_txt',
        text='You might sit too far away. Please sit closer to your screen.\n\nWe will find out your current distance. When you are ready, press spacebar to continue.',
        font='Arial',
        pos=(0, 0), height=28.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-2.0);
    InstrRedo_key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "VirtualChinrest_Redo" ---
    loading_redo = visual.TextStim(win=win, name='loading_redo',
        text='Please wait a second. Loading......',
        font='Arial',
        pos=(0, 0), height=24, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Instruction1" ---
    instr1_key = visual.ImageStim(
        win=win,
        name='instr1_key', 
        image='instr1_key.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(641,488),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=False, depth=0.0)
    key_instr1key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "keyPractice" ---
    # Run 'Begin Experiment' code from code_keyprac
    # intial hint text location
    hintlocation = 255;
    fixation_keyprac = visual.ShapeStim(
        win=win, name='fixation_keyprac',
        size=(20, 20), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    letterT = visual.ImageStim(
        win=win,
        name='letterT', 
        image='T.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), size=(80, 80),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-2.0)
    keyHint = visual.TextStim(win=win, name='keyHint',
        text='A key (tip of T facing left), S key (facing right)',
        font='Arial',
        pos=[0,0], height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    key_keyprac = keyboard.Keyboard()
    
    # --- Initialize components for Routine "keyPracFeedback" ---
    keyFeedback = visual.TextStim(win=win, name='keyFeedback',
        text='',
        font='Arial',
        pos=(0, 0), height=32, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from code_endkeyprac
    sumaccKeyPrac = 0;
    
    # --- Initialize components for Routine "Instruction2" ---
    instr2_search = visual.ImageStim(
        win=win,
        name='instr2_search', 
        image='instr2_search.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(594,465),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=False, depth=0.0)
    key_instr2search = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Instruction3" ---
    instr3_fix = visual.ImageStim(
        win=win,
        name='instr3_fix', 
        image='instr3_fix.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(501,234),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=False, depth=0.0)
    key_instr3fix = keyboard.Keyboard()
    
    # --- Initialize components for Routine "fixation" ---
    # Run 'Begin Experiment' code from code_fixinitial
    # initial fixation size
    fixsize = 28
    # intial hint text location
    hintlocation = 255;
    fixationPoint = visual.ImageStim(
        win=win,
        name='fixationPoint', 
        image='fixation.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    fixationHint = visual.TextStim(win=win, name='fixationHint',
        text='please click the white dot in the center to start.',
        font='Arial',
        pos=[0,0], height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    mouseintial = event.Mouse(win=win)
    x, y = [None, None]
    mouseintial.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "greenFixation" ---
    # Run 'Begin Experiment' code from code_fixinitial_2
    # initial fixation size
    fixsize = 28
    # intial hint text location
    hintlocation = 255;
    fixationPoint_2 = visual.ImageStim(
        win=win,
        name='fixationPoint_2', 
        image='greenfixation.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from code_initial
    # initial letter size
    # letter: 1 degree in CRT (57cm away)
    lettersize = 28;
    # initial aperture size
    aperturesize = 8000;
    # intial search window size
    searchsize = 482;
    # initial letter location
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
    # intial hint text location
    hintlocation = 255;
    background = visual.Rect(
        win=win, name='background',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='gray',
        opacity=None, depth=-1.0, interpolate=True)
    imageT = visual.ImageStim(
        win=win,
        name='imageT', 
        image='T.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-2.0)
    imageL1 = visual.ImageStim(
        win=win,
        name='imageL1', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-3.0)
    imageL2 = visual.ImageStim(
        win=win,
        name='imageL2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-4.0)
    imageL3 = visual.ImageStim(
        win=win,
        name='imageL3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-5.0)
    imageL4 = visual.ImageStim(
        win=win,
        name='imageL4', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-6.0)
    imageL5 = visual.ImageStim(
        win=win,
        name='imageL5', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-7.0)
    imageL6 = visual.ImageStim(
        win=win,
        name='imageL6', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-8.0)
    imageL7 = visual.ImageStim(
        win=win,
        name='imageL7', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-9.0)
    imageL8 = visual.ImageStim(
        win=win,
        name='imageL8', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-10.0)
    imageL9 = visual.ImageStim(
        win=win,
        name='imageL9', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-11.0)
    imageL10 = visual.ImageStim(
        win=win,
        name='imageL10', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-12.0)
    imageL11 = visual.ImageStim(
        win=win,
        name='imageL11', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-13.0)
    imageAperture = visual.ImageStim(
        win=win,
        name='imageAperture', 
        image='plainBackground.png', mask='circleMask.png', anchor='center',
        ori=0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-14.0)
    CenterAperture = visual.ImageStim(
        win=win,
        name='CenterAperture', 
        image='plainBackground.png', mask='circleMask.png', anchor='center',
        ori=0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-15.0)
    searchHint = visual.TextStim(win=win, name='searchHint',
        text='',
        font='Arial',
        pos=[0,0], height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-16.0);
    key_respMain = keyboard.Keyboard()
    
    # --- Initialize components for Routine "trialFeedback" ---
    textFeedback = visual.TextStim(win=win, name='textFeedback',
        text='',
        font='Arial',
        pos=(0, 0), height=32, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "CheckInstr" ---
    text_checkInstr = visual.TextStim(win=win, name='text_checkInstr',
        text='End of practice. To make sure you understand the instructions, we have a question for you.\n\nNow suppose the tip of letter T points toward left, like this:\n\n\n\n\n\n\n\nWhich button will your press?\n\nPress A or S key to respond.',
        font='Arial',
        pos=(0, 0), height=24, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    checkIntr_example = visual.ImageStim(
        win=win,
        name='checkIntr_example', 
        image='T.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(60, 60),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=False, depth=-1.0)
    key_checkInstr = keyboard.Keyboard()
    
    # --- Initialize components for Routine "CheckInstr_FB" ---
    feedback_CheckInstr1 = visual.TextStim(win=win, name='feedback_CheckInstr1',
        text='',
        font='Arial',
        pos=(0, 0), height=24, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    feedback_CheckInstr2 = visual.TextStim(win=win, name='feedback_CheckInstr2',
        text='Please press spacebar to continue.\n',
        font='Arial',
        pos=(0, -70), height=24, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_feedbackCheckInstr = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Instruction_MainExp" ---
    InstrMainExp = visual.TextStim(win=win, name='InstrMainExp',
        text='Now we begin the real experiment!\n\nThe task is the same as the practice you just did: click the white dot to start, then move your mouse around to find letter T. This experiment takes about 15 minutes. There are 24 blocks. At the end of each block, you will see your response accuracy and can take a short break. \n\nPlease respond as accurately and quickly as possible, and try to keep the same pose during experiment.\n\nReady? Press spacebar to start!',
        font='Arial',
        pos=(0, 0), height=24, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_InstrMainExp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "fixation" ---
    # Run 'Begin Experiment' code from code_fixinitial
    # initial fixation size
    fixsize = 28
    # intial hint text location
    hintlocation = 255;
    fixationPoint = visual.ImageStim(
        win=win,
        name='fixationPoint', 
        image='fixation.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    fixationHint = visual.TextStim(win=win, name='fixationHint',
        text='please click the white dot in the center to start.',
        font='Arial',
        pos=[0,0], height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    mouseintial = event.Mouse(win=win)
    x, y = [None, None]
    mouseintial.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "greenFixation" ---
    # Run 'Begin Experiment' code from code_fixinitial_2
    # initial fixation size
    fixsize = 28
    # intial hint text location
    hintlocation = 255;
    fixationPoint_2 = visual.ImageStim(
        win=win,
        name='fixationPoint_2', 
        image='greenfixation.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from code_initial
    # initial letter size
    # letter: 1 degree in CRT (57cm away)
    lettersize = 28;
    # initial aperture size
    aperturesize = 8000;
    # intial search window size
    searchsize = 482;
    # initial letter location
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
    # intial hint text location
    hintlocation = 255;
    background = visual.Rect(
        win=win, name='background',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='gray',
        opacity=None, depth=-1.0, interpolate=True)
    imageT = visual.ImageStim(
        win=win,
        name='imageT', 
        image='T.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-2.0)
    imageL1 = visual.ImageStim(
        win=win,
        name='imageL1', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-3.0)
    imageL2 = visual.ImageStim(
        win=win,
        name='imageL2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-4.0)
    imageL3 = visual.ImageStim(
        win=win,
        name='imageL3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-5.0)
    imageL4 = visual.ImageStim(
        win=win,
        name='imageL4', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-6.0)
    imageL5 = visual.ImageStim(
        win=win,
        name='imageL5', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-7.0)
    imageL6 = visual.ImageStim(
        win=win,
        name='imageL6', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-8.0)
    imageL7 = visual.ImageStim(
        win=win,
        name='imageL7', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-9.0)
    imageL8 = visual.ImageStim(
        win=win,
        name='imageL8', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-10.0)
    imageL9 = visual.ImageStim(
        win=win,
        name='imageL9', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-11.0)
    imageL10 = visual.ImageStim(
        win=win,
        name='imageL10', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-12.0)
    imageL11 = visual.ImageStim(
        win=win,
        name='imageL11', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-13.0)
    imageAperture = visual.ImageStim(
        win=win,
        name='imageAperture', 
        image='plainBackground.png', mask='circleMask.png', anchor='center',
        ori=0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-14.0)
    CenterAperture = visual.ImageStim(
        win=win,
        name='CenterAperture', 
        image='plainBackground.png', mask='circleMask.png', anchor='center',
        ori=0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-15.0)
    searchHint = visual.TextStim(win=win, name='searchHint',
        text='',
        font='Arial',
        pos=[0,0], height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-16.0);
    key_respMain = keyboard.Keyboard()
    
    # --- Initialize components for Routine "trialFeedback" ---
    textFeedback = visual.TextStim(win=win, name='textFeedback',
        text='',
        font='Arial',
        pos=(0, 0), height=32, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "TakeABreak" ---
    # Run 'Begin Experiment' code from code_break
    sumcorr = 0;
    avgcorr = 0;
    sumrt = 0;
    avgrt = 0;
    accfbcolor = 'white';
    rtfbcolor = 'white';
    accfbtext = "na";
    rtfbtext = "na";
    acctext = visual.TextStim(win=win, name='acctext',
        text='',
        font='Arial',
        pos=(0, 120), height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-1.0);
    rttext = visual.TextStim(win=win, name='rttext',
        text='',
        font='Arial',
        pos=(0, 60), height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-2.0);
    textBreak = visual.TextStim(win=win, name='textBreak',
        text='There are 24 blocks altogether. The number of remaining blocks is:\n\n\nPress spacebar to continue. ',
        font='Arial',
        pos=(0, -50), height=24, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    textBlockRemaining = visual.TextStim(win=win, name='textBlockRemaining',
        text='',
        font='Arial',
        pos=[0,0], height=24, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    key_respBreak = keyboard.Keyboard()
    
    # --- Initialize components for Routine "fixation" ---
    # Run 'Begin Experiment' code from code_fixinitial
    # initial fixation size
    fixsize = 28
    # intial hint text location
    hintlocation = 255;
    fixationPoint = visual.ImageStim(
        win=win,
        name='fixationPoint', 
        image='fixation.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    fixationHint = visual.TextStim(win=win, name='fixationHint',
        text='please click the white dot in the center to start.',
        font='Arial',
        pos=[0,0], height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    mouseintial = event.Mouse(win=win)
    x, y = [None, None]
    mouseintial.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "greenFixation" ---
    # Run 'Begin Experiment' code from code_fixinitial_2
    # initial fixation size
    fixsize = 28
    # intial hint text location
    hintlocation = 255;
    fixationPoint_2 = visual.ImageStim(
        win=win,
        name='fixationPoint_2', 
        image='greenfixation.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    
    # --- Initialize components for Routine "displayTestingPhase" ---
    # Run 'Begin Experiment' code from code_initial_3
    # initial letter size
    # letter: 1 degree in CRT (57cm away)
    lettersize = 28;
    # initial aperture size
    aperturesize = 8000;
    # intial search window size
    searchsize = 482;
    # initial letter location
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
    # intial hint text location
    hintlocation = 255;
    background_3 = visual.Rect(
        win=win, name='background_3',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='gray',
        opacity=None, depth=-1.0, interpolate=True)
    imageT_3 = visual.ImageStim(
        win=win,
        name='imageT_3', 
        image='T.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-2.0)
    imageL1_3 = visual.ImageStim(
        win=win,
        name='imageL1_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-3.0)
    imageL2_3 = visual.ImageStim(
        win=win,
        name='imageL2_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-4.0)
    imageL3_3 = visual.ImageStim(
        win=win,
        name='imageL3_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-5.0)
    imageL4_3 = visual.ImageStim(
        win=win,
        name='imageL4_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-6.0)
    imageL5_3 = visual.ImageStim(
        win=win,
        name='imageL5_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-7.0)
    imageL6_3 = visual.ImageStim(
        win=win,
        name='imageL6_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-8.0)
    imageL7_3 = visual.ImageStim(
        win=win,
        name='imageL7_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-9.0)
    imageL8_3 = visual.ImageStim(
        win=win,
        name='imageL8_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-10.0)
    imageL9_3 = visual.ImageStim(
        win=win,
        name='imageL9_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-11.0)
    imageL10_3 = visual.ImageStim(
        win=win,
        name='imageL10_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-12.0)
    imageL11_3 = visual.ImageStim(
        win=win,
        name='imageL11_3', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-13.0)
    imageAperture_3 = visual.ImageStim(
        win=win,
        name='imageAperture_3', 
        image='plainBackground.png', mask='circleMask.png', anchor='center',
        ori=0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-14.0)
    CenterAperture_3 = visual.ImageStim(
        win=win,
        name='CenterAperture_3', 
        image='plainBackground.png', mask='circleMask.png', anchor='center',
        ori=0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-15.0)
    key_respTesting = keyboard.Keyboard()
    
    # --- Initialize components for Routine "trialFeedback" ---
    textFeedback = visual.TextStim(win=win, name='textFeedback',
        text='',
        font='Arial',
        pos=(0, 0), height=32, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "TakeABreak2" ---
    # Run 'Begin Experiment' code from code_break2
    sumcorr = 0;
    avgcorr = 0;
    sumrt = 0;
    avgrt = 0;
    accfbcolor = 'white';
    rtfbcolor = 'white';
    accfbtext = "na";
    rtfbtext = "na";
    accText = visual.TextStim(win=win, name='accText',
        text='',
        font='Arial',
        pos=(0, 120), height=24.0, wrapWidth=None, ori=0.0, 
        color=accfbcolor, colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-1.0);
    rtText = visual.TextStim(win=win, name='rtText',
        text='',
        font='Arial',
        pos=(0, 60), height=24.0, wrapWidth=None, ori=0.0, 
        color=rtfbcolor, colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-2.0);
    TextBreak = visual.TextStim(win=win, name='TextBreak',
        text='There are 24 blocks altogether. The number of remaining blocks is:\n\n\nPress spacebar to continue. ',
        font='Arial',
        pos=(0, -50), height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-3.0);
    textblockRemaining = visual.TextStim(win=win, name='textblockRemaining',
        text='',
        font='Arial',
        pos=[0,0], height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-4.0);
    key_RespBreak = keyboard.Keyboard()
    
    # --- Initialize components for Routine "RecogQuestion" ---
    Ques_text = visual.TextStim(win=win, name='Ques_text',
        text='Thank you for completing the experiment! Here is a question for you.\n\nDuring the experiment, did you notice that some displays are repeatedly presented across blocks? \n\nPlease press Y for yes, N for no if you did not notice any repeated displays.\n\n',
        font='Arial',
        pos=(0, 0), height=24.0, wrapWidth=None, ori=None, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_AnswerQues = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Disclose" ---
    Disclose_text = visual.TextStim(win=win, name='Disclose_text',
        text='Thank you for your answer.\n\nIn fact, some displays are repeatedly presented across blocks in the experiment!\n\nPress spacebar to continue.',
        font='Arial',
        pos=(0, 0), height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    continue_key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "InstrRT" ---
    InstrRecognitionTest = visual.TextStim(win=win, name='InstrRecognitionTest',
        text='At the end, your task is to indicate whether you have seen the following displays during the course of the experiment or not. \n\nPlease respond as accurately as possible by using the Y key (Yes I have) and N key (No I have not).\n\nReady? Press spacebar to start!',
        font='Arial',
        pos=(0, 0), height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    InstrRecognitionTest_key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "fixation_RT" ---
    # Run 'Begin Experiment' code from code_RTfix
    # initial fixation size
    fixsize = 28
    # intial hint text location
    hintlocation = 255;
    fixation_image = visual.ImageStim(
        win=win,
        name='fixation_image', 
        image='fixation.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    fixationHint_text = visual.TextStim(win=win, name='fixationHint_text',
        text='please click the white dot in the center to start.',
        font='Arial',
        pos=[0,0], height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    mouseInitial = event.Mouse(win=win)
    x, y = [None, None]
    mouseInitial.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "displayRT" ---
    # Run 'Begin Experiment' code from code_initial_2
    # initial letter size
    # letter: 1 degree in CRT (57cm away)
    lettersize = 28;
    # initial aperture size
    aperturesize = 8000;
    # intial search window size
    searchsize = 482;
    # initial letter location
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
    # intial hint text location
    hintlocation = 255;
    background_2 = visual.Rect(
        win=win, name='background_2',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='gray',
        opacity=None, depth=-1.0, interpolate=True)
    imageT_2 = visual.ImageStim(
        win=win,
        name='imageT_2', 
        image='T.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-2.0)
    imageL1_2 = visual.ImageStim(
        win=win,
        name='imageL1_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-3.0)
    imageL2_2 = visual.ImageStim(
        win=win,
        name='imageL2_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-4.0)
    imageL3_2 = visual.ImageStim(
        win=win,
        name='imageL3_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-5.0)
    imageL4_2 = visual.ImageStim(
        win=win,
        name='imageL4_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-6.0)
    imageL5_2 = visual.ImageStim(
        win=win,
        name='imageL5_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-7.0)
    imageL6_2 = visual.ImageStim(
        win=win,
        name='imageL6_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-8.0)
    imageL7_2 = visual.ImageStim(
        win=win,
        name='imageL7_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-9.0)
    imageL8_2 = visual.ImageStim(
        win=win,
        name='imageL8_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-10.0)
    imageL9_2 = visual.ImageStim(
        win=win,
        name='imageL9_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-11.0)
    imageL10_2 = visual.ImageStim(
        win=win,
        name='imageL10_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-12.0)
    imageL11_2 = visual.ImageStim(
        win=win,
        name='imageL11_2', 
        image='L.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=False, depth=-13.0)
    imageAperture_2 = visual.ImageStim(
        win=win,
        name='imageAperture_2', 
        image='plainBackground.png', mask='circleMask.png', anchor='center',
        ori=0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-14.0)
    CenterAperture_2 = visual.ImageStim(
        win=win,
        name='CenterAperture_2', 
        image='plainBackground.png', mask='circleMask.png', anchor='center',
        ori=0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-15.0)
    key_respRT = keyboard.Keyboard()
    adjustHint_text = visual.TextStim(win=win, name='adjustHint_text',
        text='',
        font='Arial',
        pos=[0,0], height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    
    # --- Initialize components for Routine "EndOfExperiment" ---
    textEnd = visual.TextStim(win=win, name='textEnd',
        text='You are all done! Thank you very much for doing the experiment!\n\nTo obtain payment, please wait until you can click [OK] button to get the Prolific Completion Code.',
        font='Arial',
        pos=(0, 0), height=24, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "InstrStartPage" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('InstrStartPage.started', globalClock.getTime())
    InstrStartPage_key.keys = []
    InstrStartPage_key.rt = []
    _InstrStartPage_key_allKeys = []
    # keep track of which components have finished
    InstrStartPageComponents = [InstrStartPage_text, InstrStartPage_key]
    for thisComponent in InstrStartPageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstrStartPage" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrStartPage_text* updates
        
        # if InstrStartPage_text is starting this frame...
        if InstrStartPage_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrStartPage_text.frameNStart = frameN  # exact frame index
            InstrStartPage_text.tStart = t  # local t and not account for scr refresh
            InstrStartPage_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrStartPage_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstrStartPage_text.status = STARTED
            InstrStartPage_text.setAutoDraw(True)
        
        # if InstrStartPage_text is active this frame...
        if InstrStartPage_text.status == STARTED:
            # update params
            pass
        
        # *InstrStartPage_key* updates
        waitOnFlip = False
        
        # if InstrStartPage_key is starting this frame...
        if InstrStartPage_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrStartPage_key.frameNStart = frameN  # exact frame index
            InstrStartPage_key.tStart = t  # local t and not account for scr refresh
            InstrStartPage_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrStartPage_key, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstrStartPage_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstrStartPage_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstrStartPage_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstrStartPage_key.status == STARTED and not waitOnFlip:
            theseKeys = InstrStartPage_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _InstrStartPage_key_allKeys.extend(theseKeys)
            if len(_InstrStartPage_key_allKeys):
                InstrStartPage_key.keys = _InstrStartPage_key_allKeys[-1].name  # just the last key pressed
                InstrStartPage_key.rt = _InstrStartPage_key_allKeys[-1].rt
                InstrStartPage_key.duration = _InstrStartPage_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrStartPageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstrStartPage" ---
    for thisComponent in InstrStartPageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('InstrStartPage.stopped', globalClock.getTime())
    # the Routine "InstrStartPage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "VirtualChinrest" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('VirtualChinrest.started', globalClock.getTime())
    # Run 'Begin Routine' code from skip_offline
    #skip this component offline
    continueRoutine = True
    # keep track of which components have finished
    VirtualChinrestComponents = [loading]
    for thisComponent in VirtualChinrestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "VirtualChinrest" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *loading* updates
        
        # if loading is starting this frame...
        if loading.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loading.frameNStart = frameN  # exact frame index
            loading.tStart = t  # local t and not account for scr refresh
            loading.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loading, 'tStartRefresh')  # time at next scr refresh
            # update status
            loading.status = STARTED
            loading.setAutoDraw(True)
        
        # if loading is active this frame...
        if loading.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VirtualChinrestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "VirtualChinrest" ---
    for thisComponent in VirtualChinrestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('VirtualChinrest.stopped', globalClock.getTime())
    # the Routine "VirtualChinrest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "InstrRedo" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('InstrRedo.started', globalClock.getTime())
    # Run 'Begin Routine' code from skip_offline_2
    #skip this component offline
    continueRoutine = True
    # Run 'Begin Routine' code from code_RedoInstr
    # if ratio is higher than the maximum ratio, redo virtual chinrest
    continueRoutine = False;
    if expInfo['ratio_monitor2CRT'] > 1.6:
        continueRoutine = True;
    InstrRedo_key.keys = []
    InstrRedo_key.rt = []
    _InstrRedo_key_allKeys = []
    # keep track of which components have finished
    InstrRedoComponents = [InstrRedo_txt, InstrRedo_key]
    for thisComponent in InstrRedoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstrRedo" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrRedo_txt* updates
        
        # if InstrRedo_txt is starting this frame...
        if InstrRedo_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrRedo_txt.frameNStart = frameN  # exact frame index
            InstrRedo_txt.tStart = t  # local t and not account for scr refresh
            InstrRedo_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrRedo_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstrRedo_txt.status = STARTED
            InstrRedo_txt.setAutoDraw(True)
        
        # if InstrRedo_txt is active this frame...
        if InstrRedo_txt.status == STARTED:
            # update params
            pass
        
        # *InstrRedo_key* updates
        waitOnFlip = False
        
        # if InstrRedo_key is starting this frame...
        if InstrRedo_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrRedo_key.frameNStart = frameN  # exact frame index
            InstrRedo_key.tStart = t  # local t and not account for scr refresh
            InstrRedo_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrRedo_key, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstrRedo_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstrRedo_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstrRedo_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstrRedo_key.status == STARTED and not waitOnFlip:
            theseKeys = InstrRedo_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _InstrRedo_key_allKeys.extend(theseKeys)
            if len(_InstrRedo_key_allKeys):
                InstrRedo_key.keys = _InstrRedo_key_allKeys[-1].name  # just the last key pressed
                InstrRedo_key.rt = _InstrRedo_key_allKeys[-1].rt
                InstrRedo_key.duration = _InstrRedo_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrRedoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstrRedo" ---
    for thisComponent in InstrRedoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('InstrRedo.stopped', globalClock.getTime())
    # the Routine "InstrRedo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "VirtualChinrest_Redo" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('VirtualChinrest_Redo.started', globalClock.getTime())
    # Run 'Begin Routine' code from skip_offline_redo
    #skip this component offline
    continueRoutine = False
    # Run 'Begin Routine' code from skip_redo
    #skip this component offline
    continueRoutine = False
    
    # To show whole search range 600x600 pixels on current windown size 1920x1080 and 1366x768 pixels (most common resolution)
    # the max ratio_monitor should be 768/600= 1.28
    
    # if ratio is acceptance, then skip redo virutal chinrest
    if expInfo['ratio_monitor2CRT'] <= 1.28:
        continueRoutine = False
    # keep track of which components have finished
    VirtualChinrest_RedoComponents = [loading_redo]
    for thisComponent in VirtualChinrest_RedoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "VirtualChinrest_Redo" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *loading_redo* updates
        
        # if loading_redo is starting this frame...
        if loading_redo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loading_redo.frameNStart = frameN  # exact frame index
            loading_redo.tStart = t  # local t and not account for scr refresh
            loading_redo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loading_redo, 'tStartRefresh')  # time at next scr refresh
            # update status
            loading_redo.status = STARTED
            loading_redo.setAutoDraw(True)
        
        # if loading_redo is active this frame...
        if loading_redo.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VirtualChinrest_RedoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "VirtualChinrest_Redo" ---
    for thisComponent in VirtualChinrest_RedoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('VirtualChinrest_Redo.stopped', globalClock.getTime())
    # the Routine "VirtualChinrest_Redo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruction1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction1.started', globalClock.getTime())
    key_instr1key.keys = []
    key_instr1key.rt = []
    _key_instr1key_allKeys = []
    # keep track of which components have finished
    Instruction1Components = [instr1_key, key_instr1key]
    for thisComponent in Instruction1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr1_key* updates
        
        # if instr1_key is starting this frame...
        if instr1_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr1_key.frameNStart = frameN  # exact frame index
            instr1_key.tStart = t  # local t and not account for scr refresh
            instr1_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr1_key, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr1_key.status = STARTED
            instr1_key.setAutoDraw(True)
        
        # if instr1_key is active this frame...
        if instr1_key.status == STARTED:
            # update params
            pass
        
        # *key_instr1key* updates
        waitOnFlip = False
        
        # if key_instr1key is starting this frame...
        if key_instr1key.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_instr1key.frameNStart = frameN  # exact frame index
            key_instr1key.tStart = t  # local t and not account for scr refresh
            key_instr1key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instr1key, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_instr1key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instr1key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instr1key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instr1key.status == STARTED and not waitOnFlip:
            theseKeys = key_instr1key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instr1key_allKeys.extend(theseKeys)
            if len(_key_instr1key_allKeys):
                key_instr1key.keys = _key_instr1key_allKeys[-1].name  # just the last key pressed
                key_instr1key.rt = _key_instr1key_allKeys[-1].rt
                key_instr1key.duration = _key_instr1key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction1" ---
    for thisComponent in Instruction1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction1.stopped', globalClock.getTime())
    # the Routine "Instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    keyPracLoop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Seq_keyprac.xlsx'),
        seed=None, name='keyPracLoop')
    thisExp.addLoop(keyPracLoop)  # add the loop to the experiment
    thisKeyPracLoop = keyPracLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisKeyPracLoop.rgb)
    if thisKeyPracLoop != None:
        for paramName in thisKeyPracLoop:
            globals()[paramName] = thisKeyPracLoop[paramName]
    
    for thisKeyPracLoop in keyPracLoop:
        currentLoop = keyPracLoop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisKeyPracLoop.rgb)
        if thisKeyPracLoop != None:
            for paramName in thisKeyPracLoop:
                globals()[paramName] = thisKeyPracLoop[paramName]
        
        # --- Prepare to start Routine "keyPractice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('keyPractice.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_keyprac
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        letterT.setOri(targOrientdeg)
        keyHint.setPos((0, hintlocation))
        key_keyprac.keys = []
        key_keyprac.rt = []
        _key_keyprac_allKeys = []
        # keep track of which components have finished
        keyPracticeComponents = [fixation_keyprac, letterT, keyHint, key_keyprac]
        for thisComponent in keyPracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "keyPractice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_keyprac* updates
            
            # if fixation_keyprac is starting this frame...
            if fixation_keyprac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_keyprac.frameNStart = frameN  # exact frame index
                fixation_keyprac.tStart = t  # local t and not account for scr refresh
                fixation_keyprac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_keyprac, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixation_keyprac.status = STARTED
                fixation_keyprac.setAutoDraw(True)
            
            # if fixation_keyprac is active this frame...
            if fixation_keyprac.status == STARTED:
                # update params
                pass
            
            # if fixation_keyprac is stopping this frame...
            if fixation_keyprac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_keyprac.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_keyprac.tStop = t  # not accounting for scr refresh
                    fixation_keyprac.frameNStop = frameN  # exact frame index
                    # update status
                    fixation_keyprac.status = FINISHED
                    fixation_keyprac.setAutoDraw(False)
            
            # *letterT* updates
            
            # if letterT is starting this frame...
            if letterT.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                letterT.frameNStart = frameN  # exact frame index
                letterT.tStart = t  # local t and not account for scr refresh
                letterT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(letterT, 'tStartRefresh')  # time at next scr refresh
                # update status
                letterT.status = STARTED
                letterT.setAutoDraw(True)
            
            # if letterT is active this frame...
            if letterT.status == STARTED:
                # update params
                pass
            
            # *keyHint* updates
            
            # if keyHint is starting this frame...
            if keyHint.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                keyHint.frameNStart = frameN  # exact frame index
                keyHint.tStart = t  # local t and not account for scr refresh
                keyHint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyHint, 'tStartRefresh')  # time at next scr refresh
                # update status
                keyHint.status = STARTED
                keyHint.setAutoDraw(True)
            
            # if keyHint is active this frame...
            if keyHint.status == STARTED:
                # update params
                pass
            
            # *key_keyprac* updates
            waitOnFlip = False
            
            # if key_keyprac is starting this frame...
            if key_keyprac.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_keyprac.frameNStart = frameN  # exact frame index
                key_keyprac.tStart = t  # local t and not account for scr refresh
                key_keyprac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_keyprac, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_keyprac.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_keyprac.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_keyprac.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_keyprac.status == STARTED and not waitOnFlip:
                theseKeys = key_keyprac.getKeys(keyList=['a','s'], ignoreKeys=["escape"], waitRelease=False)
                _key_keyprac_allKeys.extend(theseKeys)
                if len(_key_keyprac_allKeys):
                    key_keyprac.keys = _key_keyprac_allKeys[0].name  # just the first key pressed
                    key_keyprac.rt = _key_keyprac_allKeys[0].rt
                    key_keyprac.duration = _key_keyprac_allKeys[0].duration
                    # was this correct?
                    if (key_keyprac.keys == str(corrAnswer)) or (key_keyprac.keys == corrAnswer):
                        key_keyprac.corr = 1
                    else:
                        key_keyprac.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in keyPracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "keyPractice" ---
        for thisComponent in keyPracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('keyPractice.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_keyprac
        if key_keyprac.corr == 1:
            keyprac_fbtext = 'correct!'
            keyprac_fbcolor = 'green';
            keyprac_fbdur = .5;
        else:
            keyprac_fbtext = 'incorrect!'
            keyprac_fbcolor = 'red';
            keyprac_fbdur = .5;
        
        # check responses
        if key_keyprac.keys in ['', [], None]:  # No response was made
            key_keyprac.keys = None
            # was no response the correct answer?!
            if str(corrAnswer).lower() == 'none':
               key_keyprac.corr = 1;  # correct non-response
            else:
               key_keyprac.corr = 0;  # failed to respond (incorrectly)
        # store data for keyPracLoop (TrialHandler)
        keyPracLoop.addData('key_keyprac.keys',key_keyprac.keys)
        keyPracLoop.addData('key_keyprac.corr', key_keyprac.corr)
        if key_keyprac.keys != None:  # we had a response
            keyPracLoop.addData('key_keyprac.rt', key_keyprac.rt)
            keyPracLoop.addData('key_keyprac.duration', key_keyprac.duration)
        # the Routine "keyPractice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "keyPracFeedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('keyPracFeedback.started', globalClock.getTime())
        keyFeedback.setColor(keyprac_fbcolor, colorSpace='rgb')
        keyFeedback.setText(keyprac_fbtext)
        # keep track of which components have finished
        keyPracFeedbackComponents = [keyFeedback]
        for thisComponent in keyPracFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "keyPracFeedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *keyFeedback* updates
            
            # if keyFeedback is starting this frame...
            if keyFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyFeedback.frameNStart = frameN  # exact frame index
                keyFeedback.tStart = t  # local t and not account for scr refresh
                keyFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyFeedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                keyFeedback.status = STARTED
                keyFeedback.setAutoDraw(True)
            
            # if keyFeedback is active this frame...
            if keyFeedback.status == STARTED:
                # update params
                pass
            
            # if keyFeedback is stopping this frame...
            if keyFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyFeedback.tStartRefresh + keyprac_fbdur-frameTolerance:
                    # keep track of stop time/frame for later
                    keyFeedback.tStop = t  # not accounting for scr refresh
                    keyFeedback.frameNStop = frameN  # exact frame index
                    # update status
                    keyFeedback.status = FINISHED
                    keyFeedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in keyPracFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "keyPracFeedback" ---
        for thisComponent in keyPracFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('keyPracFeedback.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_endkeyprac
        sumaccKeyPrac = sumaccKeyPrac + key_keyprac.corr;
        if sumaccKeyPrac >= 6:
            keyPracLoop.finished= True
        # the Routine "keyPracFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'keyPracLoop'
    
    
    # --- Prepare to start Routine "Instruction2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction2.started', globalClock.getTime())
    key_instr2search.keys = []
    key_instr2search.rt = []
    _key_instr2search_allKeys = []
    # keep track of which components have finished
    Instruction2Components = [instr2_search, key_instr2search]
    for thisComponent in Instruction2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr2_search* updates
        
        # if instr2_search is starting this frame...
        if instr2_search.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr2_search.frameNStart = frameN  # exact frame index
            instr2_search.tStart = t  # local t and not account for scr refresh
            instr2_search.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr2_search, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr2_search.status = STARTED
            instr2_search.setAutoDraw(True)
        
        # if instr2_search is active this frame...
        if instr2_search.status == STARTED:
            # update params
            pass
        
        # *key_instr2search* updates
        waitOnFlip = False
        
        # if key_instr2search is starting this frame...
        if key_instr2search.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_instr2search.frameNStart = frameN  # exact frame index
            key_instr2search.tStart = t  # local t and not account for scr refresh
            key_instr2search.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instr2search, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_instr2search.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instr2search.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instr2search.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instr2search.status == STARTED and not waitOnFlip:
            theseKeys = key_instr2search.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instr2search_allKeys.extend(theseKeys)
            if len(_key_instr2search_allKeys):
                key_instr2search.keys = _key_instr2search_allKeys[-1].name  # just the last key pressed
                key_instr2search.rt = _key_instr2search_allKeys[-1].rt
                key_instr2search.duration = _key_instr2search_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction2" ---
    for thisComponent in Instruction2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction2.stopped', globalClock.getTime())
    # the Routine "Instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruction3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction3.started', globalClock.getTime())
    key_instr3fix.keys = []
    key_instr3fix.rt = []
    _key_instr3fix_allKeys = []
    # keep track of which components have finished
    Instruction3Components = [instr3_fix, key_instr3fix]
    for thisComponent in Instruction3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr3_fix* updates
        
        # if instr3_fix is starting this frame...
        if instr3_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr3_fix.frameNStart = frameN  # exact frame index
            instr3_fix.tStart = t  # local t and not account for scr refresh
            instr3_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr3_fix, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr3_fix.status = STARTED
            instr3_fix.setAutoDraw(True)
        
        # if instr3_fix is active this frame...
        if instr3_fix.status == STARTED:
            # update params
            pass
        
        # *key_instr3fix* updates
        waitOnFlip = False
        
        # if key_instr3fix is starting this frame...
        if key_instr3fix.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_instr3fix.frameNStart = frameN  # exact frame index
            key_instr3fix.tStart = t  # local t and not account for scr refresh
            key_instr3fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instr3fix, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_instr3fix.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instr3fix.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instr3fix.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instr3fix.status == STARTED and not waitOnFlip:
            theseKeys = key_instr3fix.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instr3fix_allKeys.extend(theseKeys)
            if len(_key_instr3fix_allKeys):
                key_instr3fix.keys = _key_instr3fix_allKeys[-1].name  # just the last key pressed
                key_instr3fix.rt = _key_instr3fix_allKeys[-1].rt
                key_instr3fix.duration = _key_instr3fix_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction3" ---
    for thisComponent in Instruction3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction3.stopped', globalClock.getTime())
    # the Routine "Instruction3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsPractice = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Seq_practice.xlsx'),
        seed=None, name='trialsPractice')
    thisExp.addLoop(trialsPractice)  # add the loop to the experiment
    thisTrialsPractice = trialsPractice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice.rgb)
    if thisTrialsPractice != None:
        for paramName in thisTrialsPractice:
            globals()[paramName] = thisTrialsPractice[paramName]
    
    for thisTrialsPractice in trialsPractice:
        currentLoop = trialsPractice
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice.rgb)
        if thisTrialsPractice != None:
            for paramName in thisTrialsPractice:
                globals()[paramName] = thisTrialsPractice[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_fixinitial
        win.mouseVisible = True; # show cursor
        # fixation Hint
        if phase == 'practice':
            fixationStartTime = 4;
        else:
            fixationStartTime = 10000;
        # show mouse
        win.mouseVisible = True;
        # fixation size rescale
        fixsize = 28*expInfo['ratio_monitor2CRT'];
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        fixationPoint.setSize((fixsize, fixsize))
        fixationHint.setPos((0, hintlocation))
        # setup some python lists for storing info about the mouseintial
        mouseintial.x = []
        mouseintial.y = []
        mouseintial.leftButton = []
        mouseintial.midButton = []
        mouseintial.rightButton = []
        mouseintial.time = []
        mouseintial.clicked_name = []
        gotValidClick = False  # until a click is received
        mouseintial.mouseClock.reset()
        # keep track of which components have finished
        fixationComponents = [fixationPoint, fixationHint, mouseintial]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationPoint* updates
            
            # if fixationPoint is starting this frame...
            if fixationPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationPoint.frameNStart = frameN  # exact frame index
                fixationPoint.tStart = t  # local t and not account for scr refresh
                fixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationPoint, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationPoint.status = STARTED
                fixationPoint.setAutoDraw(True)
            
            # if fixationPoint is active this frame...
            if fixationPoint.status == STARTED:
                # update params
                pass
            
            # *fixationHint* updates
            
            # if fixationHint is starting this frame...
            if fixationHint.status == NOT_STARTED and tThisFlip >= fixationStartTime-frameTolerance:
                # keep track of start time/frame for later
                fixationHint.frameNStart = frameN  # exact frame index
                fixationHint.tStart = t  # local t and not account for scr refresh
                fixationHint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationHint, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationHint.status = STARTED
                fixationHint.setAutoDraw(True)
            
            # if fixationHint is active this frame...
            if fixationHint.status == STARTED:
                # update params
                pass
            # *mouseintial* updates
            
            # if mouseintial is starting this frame...
            if mouseintial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouseintial.frameNStart = frameN  # exact frame index
                mouseintial.tStart = t  # local t and not account for scr refresh
                mouseintial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseintial, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mouseintial.started')
                # update status
                mouseintial.status = STARTED
                prevButtonState = mouseintial.getPressed()  # if button is down already this ISN'T a new click
            if mouseintial.status == STARTED:  # only update if started and not finished!
                buttons = mouseintial.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(fixationPoint, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseintial):
                                gotValidClick = True
                                mouseintial.clicked_name.append(obj.name)
                        x, y = mouseintial.getPos()
                        mouseintial.x.append(x)
                        mouseintial.y.append(y)
                        buttons = mouseintial.getPressed()
                        mouseintial.leftButton.append(buttons[0])
                        mouseintial.midButton.append(buttons[1])
                        mouseintial.rightButton.append(buttons[2])
                        mouseintial.time.append(mouseintial.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_fixinitial
        mouselocation = [0, 0];
        thisExp.addData('fixationSize',fixsize)
        # store data for trialsPractice (TrialHandler)
        trialsPractice.addData('mouseintial.x', mouseintial.x)
        trialsPractice.addData('mouseintial.y', mouseintial.y)
        trialsPractice.addData('mouseintial.leftButton', mouseintial.leftButton)
        trialsPractice.addData('mouseintial.midButton', mouseintial.midButton)
        trialsPractice.addData('mouseintial.rightButton', mouseintial.rightButton)
        trialsPractice.addData('mouseintial.time', mouseintial.time)
        trialsPractice.addData('mouseintial.clicked_name', mouseintial.clicked_name)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "greenFixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('greenFixation.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_fixinitial_2
        win.mouseVisible = True; # show cursor
        # fixation Hint
        if phase == 'practice':
            fixationStartTime = 4;
        else:
            fixationStartTime = 10000;
        # show mouse
        win.mouseVisible = True;
        # fixation size rescale
        fixsize = 28*expInfo['ratio_monitor2CRT'];
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        fixationPoint_2.setSize((fixsize, fixsize))
        # keep track of which components have finished
        greenFixationComponents = [fixationPoint_2]
        for thisComponent in greenFixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "greenFixation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationPoint_2* updates
            
            # if fixationPoint_2 is starting this frame...
            if fixationPoint_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationPoint_2.frameNStart = frameN  # exact frame index
                fixationPoint_2.tStart = t  # local t and not account for scr refresh
                fixationPoint_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationPoint_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationPoint_2.status = STARTED
                fixationPoint_2.setAutoDraw(True)
            
            # if fixationPoint_2 is active this frame...
            if fixationPoint_2.status == STARTED:
                # update params
                pass
            
            # if fixationPoint_2 is stopping this frame...
            if fixationPoint_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationPoint_2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationPoint_2.tStop = t  # not accounting for scr refresh
                    fixationPoint_2.frameNStop = frameN  # exact frame index
                    # update status
                    fixationPoint_2.status = FINISHED
                    fixationPoint_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in greenFixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "greenFixation" ---
        for thisComponent in greenFixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('greenFixation.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_fixinitial_2
        mouselocation = [0, 0];
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.100000)
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_initial
        win.mouseVisible = True; # show cursor
        # initial first location to center
        mouselocation = [0, 0];
        whichframe = 0;
        # create empty list to save mouse location
        mouselocationlistx = [];
        mouselocationlisty = [];
        whichframelist = [];
        
        # search Hint only for practice block
        if phase == 'practice':
            searchHintStartTime = 0;
            # first practice block (block 0)
            if block == 0:
                searchHintText = 'Please find letter T and report its direction';
            else:
                searchHintText = 'Please find letter T and report its direction';
        else:
            searchHintStartTime = 10000;
        
        # block 0 is the first prac block (fully visible)
        if block == 0:
            startApertureTime = 10000;
        else:
            startApertureTime = 10000;
        
        # letter size
        lettersize = 28*expInfo['ratio_monitor2CRT'];
        # aperture size
        aperturesize = 8000*expInfo['ratio_monitor2CRT'];
        # rescale search window size
        searchsize = 482*expInfo['ratio_monitor2CRT'];
        # rescale letter location
        newtlocx = tlocx * expInfo['ratio_monitor2CRT'];
        newtlocy = tlocy * expInfo['ratio_monitor2CRT'];
        newd1x = d1x * expInfo['ratio_monitor2CRT'];
        newd1y = d1y * expInfo['ratio_monitor2CRT'];
        newd2x = d2x * expInfo['ratio_monitor2CRT'];
        newd2y = d2y * expInfo['ratio_monitor2CRT'];
        newd3x = d3x * expInfo['ratio_monitor2CRT'];
        newd3y = d3y * expInfo['ratio_monitor2CRT'];
        newd4x = d4x * expInfo['ratio_monitor2CRT'];
        newd4y = d4y * expInfo['ratio_monitor2CRT'];
        newd5x = d5x * expInfo['ratio_monitor2CRT'];
        newd5y = d5y * expInfo['ratio_monitor2CRT'];
        newd6x = d6x * expInfo['ratio_monitor2CRT'];
        newd6y = d6y * expInfo['ratio_monitor2CRT'];
        newd7x = d7x * expInfo['ratio_monitor2CRT'];
        newd7y = d7y * expInfo['ratio_monitor2CRT'];
        newd8x = d8x * expInfo['ratio_monitor2CRT'];
        newd8y = d8y * expInfo['ratio_monitor2CRT'];
        newd9x = d9x * expInfo['ratio_monitor2CRT'];
        newd9y = d9y * expInfo['ratio_monitor2CRT'];
        newd10x = d10x * expInfo['ratio_monitor2CRT'];
        newd10y = d10y * expInfo['ratio_monitor2CRT'];
        newd11x = d11x * expInfo['ratio_monitor2CRT'];
        newd11y = d11y * expInfo['ratio_monitor2CRT'];
        
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        background.setSize((searchsize, searchsize))
        imageT.setPos((newtlocx, newtlocy))
        imageT.setSize((lettersize, lettersize))
        imageT.setOri(targOrientdeg)
        imageL1.setPos((newd1x,newd1y))
        imageL1.setSize((lettersize, lettersize))
        imageL1.setOri(d1Orient)
        imageL2.setPos((newd2x,newd2y))
        imageL2.setSize((lettersize, lettersize))
        imageL2.setOri(d2Orient)
        imageL3.setPos((newd3x,newd3y))
        imageL3.setSize((lettersize, lettersize))
        imageL3.setOri(d3Orient)
        imageL4.setPos((newd4x,newd4y))
        imageL4.setSize((lettersize, lettersize))
        imageL4.setOri(d4Orient)
        imageL5.setPos((newd5x,newd5y))
        imageL5.setSize((lettersize, lettersize))
        imageL5.setOri(d5Orient)
        imageL6.setPos((newd6x,newd6y))
        imageL6.setSize((lettersize, lettersize))
        imageL6.setOri(d6Orient)
        imageL7.setPos((newd7x,newd7y))
        imageL7.setSize((lettersize, lettersize))
        imageL7.setOri(d7Orient)
        imageL8.setPos((newd8x,newd8y))
        imageL8.setSize((lettersize, lettersize))
        imageL8.setOri(d8Orient)
        imageL9.setPos((newd9x,newd9y))
        imageL9.setSize((lettersize, lettersize))
        imageL9.setOri(d9Orient)
        imageL10.setPos((newd10x,newd10y))
        imageL10.setSize((lettersize, lettersize))
        imageL10.setOri(d10Orient)
        imageL11.setPos((newd11x,newd11y))
        imageL11.setSize((lettersize, lettersize))
        imageL11.setOri(d11Orient)
        imageAperture.setSize((aperturesize, aperturesize))
        CenterAperture.setPos([0, 0])
        CenterAperture.setSize((aperturesize, aperturesize))
        searchHint.setPos((0, hintlocation))
        searchHint.setText(searchHintText)
        key_respMain.keys = []
        key_respMain.rt = []
        _key_respMain_allKeys = []
        # keep track of which components have finished
        trialComponents = [background, imageT, imageL1, imageL2, imageL3, imageL4, imageL5, imageL6, imageL7, imageL8, imageL9, imageL10, imageL11, imageAperture, CenterAperture, searchHint, key_respMain]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background* updates
            
            # if background is starting this frame...
            if background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background.frameNStart = frameN  # exact frame index
                background.tStart = t  # local t and not account for scr refresh
                background.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background.started')
                # update status
                background.status = STARTED
                background.setAutoDraw(True)
            
            # if background is active this frame...
            if background.status == STARTED:
                # update params
                pass
            
            # *imageT* updates
            
            # if imageT is starting this frame...
            if imageT.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageT.frameNStart = frameN  # exact frame index
                imageT.tStart = t  # local t and not account for scr refresh
                imageT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageT, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageT.status = STARTED
                imageT.setAutoDraw(True)
            
            # if imageT is active this frame...
            if imageT.status == STARTED:
                # update params
                pass
            
            # *imageL1* updates
            
            # if imageL1 is starting this frame...
            if imageL1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL1.frameNStart = frameN  # exact frame index
                imageL1.tStart = t  # local t and not account for scr refresh
                imageL1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL1, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL1.status = STARTED
                imageL1.setAutoDraw(True)
            
            # if imageL1 is active this frame...
            if imageL1.status == STARTED:
                # update params
                pass
            
            # *imageL2* updates
            
            # if imageL2 is starting this frame...
            if imageL2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL2.frameNStart = frameN  # exact frame index
                imageL2.tStart = t  # local t and not account for scr refresh
                imageL2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL2.status = STARTED
                imageL2.setAutoDraw(True)
            
            # if imageL2 is active this frame...
            if imageL2.status == STARTED:
                # update params
                pass
            
            # *imageL3* updates
            
            # if imageL3 is starting this frame...
            if imageL3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL3.frameNStart = frameN  # exact frame index
                imageL3.tStart = t  # local t and not account for scr refresh
                imageL3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL3.status = STARTED
                imageL3.setAutoDraw(True)
            
            # if imageL3 is active this frame...
            if imageL3.status == STARTED:
                # update params
                pass
            
            # *imageL4* updates
            
            # if imageL4 is starting this frame...
            if imageL4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL4.frameNStart = frameN  # exact frame index
                imageL4.tStart = t  # local t and not account for scr refresh
                imageL4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL4, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL4.status = STARTED
                imageL4.setAutoDraw(True)
            
            # if imageL4 is active this frame...
            if imageL4.status == STARTED:
                # update params
                pass
            
            # *imageL5* updates
            
            # if imageL5 is starting this frame...
            if imageL5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL5.frameNStart = frameN  # exact frame index
                imageL5.tStart = t  # local t and not account for scr refresh
                imageL5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL5, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL5.status = STARTED
                imageL5.setAutoDraw(True)
            
            # if imageL5 is active this frame...
            if imageL5.status == STARTED:
                # update params
                pass
            
            # *imageL6* updates
            
            # if imageL6 is starting this frame...
            if imageL6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL6.frameNStart = frameN  # exact frame index
                imageL6.tStart = t  # local t and not account for scr refresh
                imageL6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL6, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL6.status = STARTED
                imageL6.setAutoDraw(True)
            
            # if imageL6 is active this frame...
            if imageL6.status == STARTED:
                # update params
                pass
            
            # *imageL7* updates
            
            # if imageL7 is starting this frame...
            if imageL7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL7.frameNStart = frameN  # exact frame index
                imageL7.tStart = t  # local t and not account for scr refresh
                imageL7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL7, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL7.status = STARTED
                imageL7.setAutoDraw(True)
            
            # if imageL7 is active this frame...
            if imageL7.status == STARTED:
                # update params
                pass
            
            # *imageL8* updates
            
            # if imageL8 is starting this frame...
            if imageL8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL8.frameNStart = frameN  # exact frame index
                imageL8.tStart = t  # local t and not account for scr refresh
                imageL8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL8, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL8.status = STARTED
                imageL8.setAutoDraw(True)
            
            # if imageL8 is active this frame...
            if imageL8.status == STARTED:
                # update params
                pass
            
            # *imageL9* updates
            
            # if imageL9 is starting this frame...
            if imageL9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL9.frameNStart = frameN  # exact frame index
                imageL9.tStart = t  # local t and not account for scr refresh
                imageL9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL9, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL9.status = STARTED
                imageL9.setAutoDraw(True)
            
            # if imageL9 is active this frame...
            if imageL9.status == STARTED:
                # update params
                pass
            
            # *imageL10* updates
            
            # if imageL10 is starting this frame...
            if imageL10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL10.frameNStart = frameN  # exact frame index
                imageL10.tStart = t  # local t and not account for scr refresh
                imageL10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL10, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL10.status = STARTED
                imageL10.setAutoDraw(True)
            
            # if imageL10 is active this frame...
            if imageL10.status == STARTED:
                # update params
                pass
            
            # *imageL11* updates
            
            # if imageL11 is starting this frame...
            if imageL11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL11.frameNStart = frameN  # exact frame index
                imageL11.tStart = t  # local t and not account for scr refresh
                imageL11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL11, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL11.status = STARTED
                imageL11.setAutoDraw(True)
            
            # if imageL11 is active this frame...
            if imageL11.status == STARTED:
                # update params
                pass
            
            # *imageAperture* updates
            
            # if imageAperture is starting this frame...
            if imageAperture.status == NOT_STARTED and tThisFlip >= startApertureTime-frameTolerance:
                # keep track of start time/frame for later
                imageAperture.frameNStart = frameN  # exact frame index
                imageAperture.tStart = t  # local t and not account for scr refresh
                imageAperture.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageAperture, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageAperture.started')
                # update status
                imageAperture.status = STARTED
                imageAperture.setAutoDraw(True)
            
            # if imageAperture is active this frame...
            if imageAperture.status == STARTED:
                # update params
                imageAperture.setPos(mouselocation, log=False)
            
            # *CenterAperture* updates
            
            # if CenterAperture is starting this frame...
            if CenterAperture.status == NOT_STARTED and tThisFlip >= startApertureTime-frameTolerance:
                # keep track of start time/frame for later
                CenterAperture.frameNStart = frameN  # exact frame index
                CenterAperture.tStart = t  # local t and not account for scr refresh
                CenterAperture.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CenterAperture, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CenterAperture.started')
                # update status
                CenterAperture.status = STARTED
                CenterAperture.setAutoDraw(True)
            
            # if CenterAperture is active this frame...
            if CenterAperture.status == STARTED:
                # update params
                pass
            
            # if CenterAperture is stopping this frame...
            if CenterAperture.status == STARTED:
                if frameN >= (CenterAperture.frameNStart + 1):
                    # keep track of stop time/frame for later
                    CenterAperture.tStop = t  # not accounting for scr refresh
                    CenterAperture.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CenterAperture.stopped')
                    # update status
                    CenterAperture.status = FINISHED
                    CenterAperture.setAutoDraw(False)
            
            # *searchHint* updates
            
            # if searchHint is starting this frame...
            if searchHint.status == NOT_STARTED and tThisFlip >= searchHintStartTime-frameTolerance:
                # keep track of start time/frame for later
                searchHint.frameNStart = frameN  # exact frame index
                searchHint.tStart = t  # local t and not account for scr refresh
                searchHint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(searchHint, 'tStartRefresh')  # time at next scr refresh
                # update status
                searchHint.status = STARTED
                searchHint.setAutoDraw(True)
            
            # if searchHint is active this frame...
            if searchHint.status == STARTED:
                # update params
                pass
            
            # *key_respMain* updates
            waitOnFlip = False
            
            # if key_respMain is starting this frame...
            if key_respMain.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_respMain.frameNStart = frameN  # exact frame index
                key_respMain.tStart = t  # local t and not account for scr refresh
                key_respMain.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respMain, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_respMain.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respMain.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respMain.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respMain.status == STARTED and not waitOnFlip:
                theseKeys = key_respMain.getKeys(keyList=['a','s'], ignoreKeys=["escape"], waitRelease=False)
                _key_respMain_allKeys.extend(theseKeys)
                if len(_key_respMain_allKeys):
                    key_respMain.keys = _key_respMain_allKeys[0].name  # just the first key pressed
                    key_respMain.rt = _key_respMain_allKeys[0].rt
                    key_respMain.duration = _key_respMain_allKeys[0].duration
                    # was this correct?
                    if (key_respMain.keys == str(corrAnswer)) or (key_respMain.keys == corrAnswer):
                        key_respMain.corr = 1
                    else:
                        key_respMain.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_initial
        thisExp.addData('letterSize',lettersize);
        thisExp.addData('apertureSize',aperturesize);
        thisExp.addData('searchsize',searchsize);
        # check responses
        if key_respMain.keys in ['', [], None]:  # No response was made
            key_respMain.keys = None
            # was no response the correct answer?!
            if str(corrAnswer).lower() == 'none':
               key_respMain.corr = 1;  # correct non-response
            else:
               key_respMain.corr = 0;  # failed to respond (incorrectly)
        # store data for trialsPractice (TrialHandler)
        trialsPractice.addData('key_respMain.keys',key_respMain.keys)
        trialsPractice.addData('key_respMain.corr', key_respMain.corr)
        if key_respMain.keys != None:  # we had a response
            trialsPractice.addData('key_respMain.rt', key_respMain.rt)
            trialsPractice.addData('key_respMain.duration', key_respMain.duration)
        # Run 'End Routine' code from code_end
        mouselocation = [0, 0];
        if key_respMain.corr == 1:
            fbtext = 'correct!'
            fbcolor = 'green';
            fbdur = .2;
        else:
            fbtext = 'incorrect!'
            fbcolor = 'red';
            fbdur = 4;
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trialFeedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trialFeedback.started', globalClock.getTime())
        textFeedback.setColor(fbcolor, colorSpace='rgb')
        textFeedback.setText(fbtext)
        # keep track of which components have finished
        trialFeedbackComponents = [textFeedback]
        for thisComponent in trialFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialFeedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textFeedback* updates
            
            # if textFeedback is starting this frame...
            if textFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFeedback.frameNStart = frameN  # exact frame index
                textFeedback.tStart = t  # local t and not account for scr refresh
                textFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFeedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                textFeedback.status = STARTED
                textFeedback.setAutoDraw(True)
            
            # if textFeedback is active this frame...
            if textFeedback.status == STARTED:
                # update params
                pass
            
            # if textFeedback is stopping this frame...
            if textFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFeedback.tStartRefresh + fbdur-frameTolerance:
                    # keep track of stop time/frame for later
                    textFeedback.tStop = t  # not accounting for scr refresh
                    textFeedback.frameNStop = frameN  # exact frame index
                    # update status
                    textFeedback.status = FINISHED
                    textFeedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialFeedback" ---
        for thisComponent in trialFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trialFeedback.stopped', globalClock.getTime())
        # the Routine "trialFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1 repeats of 'trialsPractice'
    
    
    # --- Prepare to start Routine "CheckInstr" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('CheckInstr.started', globalClock.getTime())
    key_checkInstr.keys = []
    key_checkInstr.rt = []
    _key_checkInstr_allKeys = []
    # keep track of which components have finished
    CheckInstrComponents = [text_checkInstr, checkIntr_example, key_checkInstr]
    for thisComponent in CheckInstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CheckInstr" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_checkInstr* updates
        
        # if text_checkInstr is starting this frame...
        if text_checkInstr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_checkInstr.frameNStart = frameN  # exact frame index
            text_checkInstr.tStart = t  # local t and not account for scr refresh
            text_checkInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_checkInstr, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_checkInstr.status = STARTED
            text_checkInstr.setAutoDraw(True)
        
        # if text_checkInstr is active this frame...
        if text_checkInstr.status == STARTED:
            # update params
            pass
        
        # *checkIntr_example* updates
        
        # if checkIntr_example is starting this frame...
        if checkIntr_example.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            checkIntr_example.frameNStart = frameN  # exact frame index
            checkIntr_example.tStart = t  # local t and not account for scr refresh
            checkIntr_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(checkIntr_example, 'tStartRefresh')  # time at next scr refresh
            # update status
            checkIntr_example.status = STARTED
            checkIntr_example.setAutoDraw(True)
        
        # if checkIntr_example is active this frame...
        if checkIntr_example.status == STARTED:
            # update params
            pass
        
        # *key_checkInstr* updates
        waitOnFlip = False
        
        # if key_checkInstr is starting this frame...
        if key_checkInstr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_checkInstr.frameNStart = frameN  # exact frame index
            key_checkInstr.tStart = t  # local t and not account for scr refresh
            key_checkInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_checkInstr, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_checkInstr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_checkInstr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_checkInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_checkInstr.status == STARTED and not waitOnFlip:
            theseKeys = key_checkInstr.getKeys(keyList=['a','s'], ignoreKeys=["escape"], waitRelease=False)
            _key_checkInstr_allKeys.extend(theseKeys)
            if len(_key_checkInstr_allKeys):
                key_checkInstr.keys = _key_checkInstr_allKeys[-1].name  # just the last key pressed
                key_checkInstr.rt = _key_checkInstr_allKeys[-1].rt
                key_checkInstr.duration = _key_checkInstr_allKeys[-1].duration
                # was this correct?
                if (key_checkInstr.keys == str('a')) or (key_checkInstr.keys == 'a'):
                    key_checkInstr.corr = 1
                else:
                    key_checkInstr.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CheckInstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CheckInstr" ---
    for thisComponent in CheckInstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('CheckInstr.stopped', globalClock.getTime())
    # check responses
    if key_checkInstr.keys in ['', [], None]:  # No response was made
        key_checkInstr.keys = None
        # was no response the correct answer?!
        if str('a').lower() == 'none':
           key_checkInstr.corr = 1;  # correct non-response
        else:
           key_checkInstr.corr = 0;  # failed to respond (incorrectly)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('key_checkInstr.keys',key_checkInstr.keys)
    thisExp.addData('key_checkInstr.corr', key_checkInstr.corr)
    if key_checkInstr.keys != None:  # we had a response
        thisExp.addData('key_checkInstr.rt', key_checkInstr.rt)
        thisExp.addData('key_checkInstr.duration', key_checkInstr.duration)
    thisExp.nextEntry()
    # Run 'End Routine' code from code_checkIntr
    if key_checkInstr.corr == 1:
        fbtext_checkInstr = 'Correct! Press A key when the tip of T is facing left.';
    else:
        fbtext_checkInstr = 'Incorrect! Press A key when the tip of T is facing left.';
    # the Routine "CheckInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "CheckInstr_FB" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('CheckInstr_FB.started', globalClock.getTime())
    feedback_CheckInstr1.setText(fbtext_checkInstr)
    key_feedbackCheckInstr.keys = []
    key_feedbackCheckInstr.rt = []
    _key_feedbackCheckInstr_allKeys = []
    # keep track of which components have finished
    CheckInstr_FBComponents = [feedback_CheckInstr1, feedback_CheckInstr2, key_feedbackCheckInstr]
    for thisComponent in CheckInstr_FBComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CheckInstr_FB" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_CheckInstr1* updates
        
        # if feedback_CheckInstr1 is starting this frame...
        if feedback_CheckInstr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_CheckInstr1.frameNStart = frameN  # exact frame index
            feedback_CheckInstr1.tStart = t  # local t and not account for scr refresh
            feedback_CheckInstr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_CheckInstr1, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_CheckInstr1.status = STARTED
            feedback_CheckInstr1.setAutoDraw(True)
        
        # if feedback_CheckInstr1 is active this frame...
        if feedback_CheckInstr1.status == STARTED:
            # update params
            pass
        
        # *feedback_CheckInstr2* updates
        
        # if feedback_CheckInstr2 is starting this frame...
        if feedback_CheckInstr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_CheckInstr2.frameNStart = frameN  # exact frame index
            feedback_CheckInstr2.tStart = t  # local t and not account for scr refresh
            feedback_CheckInstr2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_CheckInstr2, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_CheckInstr2.status = STARTED
            feedback_CheckInstr2.setAutoDraw(True)
        
        # if feedback_CheckInstr2 is active this frame...
        if feedback_CheckInstr2.status == STARTED:
            # update params
            pass
        
        # *key_feedbackCheckInstr* updates
        waitOnFlip = False
        
        # if key_feedbackCheckInstr is starting this frame...
        if key_feedbackCheckInstr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_feedbackCheckInstr.frameNStart = frameN  # exact frame index
            key_feedbackCheckInstr.tStart = t  # local t and not account for scr refresh
            key_feedbackCheckInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_feedbackCheckInstr, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_feedbackCheckInstr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_feedbackCheckInstr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_feedbackCheckInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_feedbackCheckInstr.status == STARTED and not waitOnFlip:
            theseKeys = key_feedbackCheckInstr.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_feedbackCheckInstr_allKeys.extend(theseKeys)
            if len(_key_feedbackCheckInstr_allKeys):
                key_feedbackCheckInstr.keys = _key_feedbackCheckInstr_allKeys[-1].name  # just the last key pressed
                key_feedbackCheckInstr.rt = _key_feedbackCheckInstr_allKeys[-1].rt
                key_feedbackCheckInstr.duration = _key_feedbackCheckInstr_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CheckInstr_FBComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CheckInstr_FB" ---
    for thisComponent in CheckInstr_FBComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('CheckInstr_FB.stopped', globalClock.getTime())
    # the Routine "CheckInstr_FB" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruction_MainExp" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction_MainExp.started', globalClock.getTime())
    key_InstrMainExp.keys = []
    key_InstrMainExp.rt = []
    _key_InstrMainExp_allKeys = []
    # keep track of which components have finished
    Instruction_MainExpComponents = [InstrMainExp, key_InstrMainExp]
    for thisComponent in Instruction_MainExpComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction_MainExp" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrMainExp* updates
        
        # if InstrMainExp is starting this frame...
        if InstrMainExp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            InstrMainExp.frameNStart = frameN  # exact frame index
            InstrMainExp.tStart = t  # local t and not account for scr refresh
            InstrMainExp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrMainExp, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstrMainExp.status = STARTED
            InstrMainExp.setAutoDraw(True)
        
        # if InstrMainExp is active this frame...
        if InstrMainExp.status == STARTED:
            # update params
            pass
        
        # *key_InstrMainExp* updates
        waitOnFlip = False
        
        # if key_InstrMainExp is starting this frame...
        if key_InstrMainExp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_InstrMainExp.frameNStart = frameN  # exact frame index
            key_InstrMainExp.tStart = t  # local t and not account for scr refresh
            key_InstrMainExp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_InstrMainExp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_InstrMainExp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_InstrMainExp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_InstrMainExp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_InstrMainExp.status == STARTED and not waitOnFlip:
            theseKeys = key_InstrMainExp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_InstrMainExp_allKeys.extend(theseKeys)
            if len(_key_InstrMainExp_allKeys):
                key_InstrMainExp.keys = _key_InstrMainExp_allKeys[-1].name  # just the last key pressed
                key_InstrMainExp.rt = _key_InstrMainExp_allKeys[-1].rt
                key_InstrMainExp.duration = _key_InstrMainExp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction_MainExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction_MainExp" ---
    for thisComponent in Instruction_MainExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction_MainExp.stopped', globalClock.getTime())
    # the Routine "Instruction_MainExp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(parameterfile),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_fixinitial
        win.mouseVisible = True; # show cursor
        # fixation Hint
        if phase == 'practice':
            fixationStartTime = 4;
        else:
            fixationStartTime = 10000;
        # show mouse
        win.mouseVisible = True;
        # fixation size rescale
        fixsize = 28*expInfo['ratio_monitor2CRT'];
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        fixationPoint.setSize((fixsize, fixsize))
        fixationHint.setPos((0, hintlocation))
        # setup some python lists for storing info about the mouseintial
        mouseintial.x = []
        mouseintial.y = []
        mouseintial.leftButton = []
        mouseintial.midButton = []
        mouseintial.rightButton = []
        mouseintial.time = []
        mouseintial.clicked_name = []
        gotValidClick = False  # until a click is received
        mouseintial.mouseClock.reset()
        # keep track of which components have finished
        fixationComponents = [fixationPoint, fixationHint, mouseintial]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationPoint* updates
            
            # if fixationPoint is starting this frame...
            if fixationPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationPoint.frameNStart = frameN  # exact frame index
                fixationPoint.tStart = t  # local t and not account for scr refresh
                fixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationPoint, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationPoint.status = STARTED
                fixationPoint.setAutoDraw(True)
            
            # if fixationPoint is active this frame...
            if fixationPoint.status == STARTED:
                # update params
                pass
            
            # *fixationHint* updates
            
            # if fixationHint is starting this frame...
            if fixationHint.status == NOT_STARTED and tThisFlip >= fixationStartTime-frameTolerance:
                # keep track of start time/frame for later
                fixationHint.frameNStart = frameN  # exact frame index
                fixationHint.tStart = t  # local t and not account for scr refresh
                fixationHint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationHint, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationHint.status = STARTED
                fixationHint.setAutoDraw(True)
            
            # if fixationHint is active this frame...
            if fixationHint.status == STARTED:
                # update params
                pass
            # *mouseintial* updates
            
            # if mouseintial is starting this frame...
            if mouseintial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouseintial.frameNStart = frameN  # exact frame index
                mouseintial.tStart = t  # local t and not account for scr refresh
                mouseintial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseintial, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mouseintial.started')
                # update status
                mouseintial.status = STARTED
                prevButtonState = mouseintial.getPressed()  # if button is down already this ISN'T a new click
            if mouseintial.status == STARTED:  # only update if started and not finished!
                buttons = mouseintial.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(fixationPoint, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseintial):
                                gotValidClick = True
                                mouseintial.clicked_name.append(obj.name)
                        x, y = mouseintial.getPos()
                        mouseintial.x.append(x)
                        mouseintial.y.append(y)
                        buttons = mouseintial.getPressed()
                        mouseintial.leftButton.append(buttons[0])
                        mouseintial.midButton.append(buttons[1])
                        mouseintial.rightButton.append(buttons[2])
                        mouseintial.time.append(mouseintial.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_fixinitial
        mouselocation = [0, 0];
        thisExp.addData('fixationSize',fixsize)
        # store data for trials (TrialHandler)
        trials.addData('mouseintial.x', mouseintial.x)
        trials.addData('mouseintial.y', mouseintial.y)
        trials.addData('mouseintial.leftButton', mouseintial.leftButton)
        trials.addData('mouseintial.midButton', mouseintial.midButton)
        trials.addData('mouseintial.rightButton', mouseintial.rightButton)
        trials.addData('mouseintial.time', mouseintial.time)
        trials.addData('mouseintial.clicked_name', mouseintial.clicked_name)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "greenFixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('greenFixation.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_fixinitial_2
        win.mouseVisible = True; # show cursor
        # fixation Hint
        if phase == 'practice':
            fixationStartTime = 4;
        else:
            fixationStartTime = 10000;
        # show mouse
        win.mouseVisible = True;
        # fixation size rescale
        fixsize = 28*expInfo['ratio_monitor2CRT'];
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        fixationPoint_2.setSize((fixsize, fixsize))
        # keep track of which components have finished
        greenFixationComponents = [fixationPoint_2]
        for thisComponent in greenFixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "greenFixation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationPoint_2* updates
            
            # if fixationPoint_2 is starting this frame...
            if fixationPoint_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationPoint_2.frameNStart = frameN  # exact frame index
                fixationPoint_2.tStart = t  # local t and not account for scr refresh
                fixationPoint_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationPoint_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationPoint_2.status = STARTED
                fixationPoint_2.setAutoDraw(True)
            
            # if fixationPoint_2 is active this frame...
            if fixationPoint_2.status == STARTED:
                # update params
                pass
            
            # if fixationPoint_2 is stopping this frame...
            if fixationPoint_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationPoint_2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationPoint_2.tStop = t  # not accounting for scr refresh
                    fixationPoint_2.frameNStop = frameN  # exact frame index
                    # update status
                    fixationPoint_2.status = FINISHED
                    fixationPoint_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in greenFixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "greenFixation" ---
        for thisComponent in greenFixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('greenFixation.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_fixinitial_2
        mouselocation = [0, 0];
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.100000)
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_initial
        win.mouseVisible = True; # show cursor
        # initial first location to center
        mouselocation = [0, 0];
        whichframe = 0;
        # create empty list to save mouse location
        mouselocationlistx = [];
        mouselocationlisty = [];
        whichframelist = [];
        
        # search Hint only for practice block
        if phase == 'practice':
            searchHintStartTime = 0;
            # first practice block (block 0)
            if block == 0:
                searchHintText = 'Please find letter T and report its direction';
            else:
                searchHintText = 'Please find letter T and report its direction';
        else:
            searchHintStartTime = 10000;
        
        # block 0 is the first prac block (fully visible)
        if block == 0:
            startApertureTime = 10000;
        else:
            startApertureTime = 10000;
        
        # letter size
        lettersize = 28*expInfo['ratio_monitor2CRT'];
        # aperture size
        aperturesize = 8000*expInfo['ratio_monitor2CRT'];
        # rescale search window size
        searchsize = 482*expInfo['ratio_monitor2CRT'];
        # rescale letter location
        newtlocx = tlocx * expInfo['ratio_monitor2CRT'];
        newtlocy = tlocy * expInfo['ratio_monitor2CRT'];
        newd1x = d1x * expInfo['ratio_monitor2CRT'];
        newd1y = d1y * expInfo['ratio_monitor2CRT'];
        newd2x = d2x * expInfo['ratio_monitor2CRT'];
        newd2y = d2y * expInfo['ratio_monitor2CRT'];
        newd3x = d3x * expInfo['ratio_monitor2CRT'];
        newd3y = d3y * expInfo['ratio_monitor2CRT'];
        newd4x = d4x * expInfo['ratio_monitor2CRT'];
        newd4y = d4y * expInfo['ratio_monitor2CRT'];
        newd5x = d5x * expInfo['ratio_monitor2CRT'];
        newd5y = d5y * expInfo['ratio_monitor2CRT'];
        newd6x = d6x * expInfo['ratio_monitor2CRT'];
        newd6y = d6y * expInfo['ratio_monitor2CRT'];
        newd7x = d7x * expInfo['ratio_monitor2CRT'];
        newd7y = d7y * expInfo['ratio_monitor2CRT'];
        newd8x = d8x * expInfo['ratio_monitor2CRT'];
        newd8y = d8y * expInfo['ratio_monitor2CRT'];
        newd9x = d9x * expInfo['ratio_monitor2CRT'];
        newd9y = d9y * expInfo['ratio_monitor2CRT'];
        newd10x = d10x * expInfo['ratio_monitor2CRT'];
        newd10y = d10y * expInfo['ratio_monitor2CRT'];
        newd11x = d11x * expInfo['ratio_monitor2CRT'];
        newd11y = d11y * expInfo['ratio_monitor2CRT'];
        
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        background.setSize((searchsize, searchsize))
        imageT.setPos((newtlocx, newtlocy))
        imageT.setSize((lettersize, lettersize))
        imageT.setOri(targOrientdeg)
        imageL1.setPos((newd1x,newd1y))
        imageL1.setSize((lettersize, lettersize))
        imageL1.setOri(d1Orient)
        imageL2.setPos((newd2x,newd2y))
        imageL2.setSize((lettersize, lettersize))
        imageL2.setOri(d2Orient)
        imageL3.setPos((newd3x,newd3y))
        imageL3.setSize((lettersize, lettersize))
        imageL3.setOri(d3Orient)
        imageL4.setPos((newd4x,newd4y))
        imageL4.setSize((lettersize, lettersize))
        imageL4.setOri(d4Orient)
        imageL5.setPos((newd5x,newd5y))
        imageL5.setSize((lettersize, lettersize))
        imageL5.setOri(d5Orient)
        imageL6.setPos((newd6x,newd6y))
        imageL6.setSize((lettersize, lettersize))
        imageL6.setOri(d6Orient)
        imageL7.setPos((newd7x,newd7y))
        imageL7.setSize((lettersize, lettersize))
        imageL7.setOri(d7Orient)
        imageL8.setPos((newd8x,newd8y))
        imageL8.setSize((lettersize, lettersize))
        imageL8.setOri(d8Orient)
        imageL9.setPos((newd9x,newd9y))
        imageL9.setSize((lettersize, lettersize))
        imageL9.setOri(d9Orient)
        imageL10.setPos((newd10x,newd10y))
        imageL10.setSize((lettersize, lettersize))
        imageL10.setOri(d10Orient)
        imageL11.setPos((newd11x,newd11y))
        imageL11.setSize((lettersize, lettersize))
        imageL11.setOri(d11Orient)
        imageAperture.setSize((aperturesize, aperturesize))
        CenterAperture.setPos([0, 0])
        CenterAperture.setSize((aperturesize, aperturesize))
        searchHint.setPos((0, hintlocation))
        searchHint.setText(searchHintText)
        key_respMain.keys = []
        key_respMain.rt = []
        _key_respMain_allKeys = []
        # keep track of which components have finished
        trialComponents = [background, imageT, imageL1, imageL2, imageL3, imageL4, imageL5, imageL6, imageL7, imageL8, imageL9, imageL10, imageL11, imageAperture, CenterAperture, searchHint, key_respMain]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background* updates
            
            # if background is starting this frame...
            if background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background.frameNStart = frameN  # exact frame index
                background.tStart = t  # local t and not account for scr refresh
                background.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background.started')
                # update status
                background.status = STARTED
                background.setAutoDraw(True)
            
            # if background is active this frame...
            if background.status == STARTED:
                # update params
                pass
            
            # *imageT* updates
            
            # if imageT is starting this frame...
            if imageT.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageT.frameNStart = frameN  # exact frame index
                imageT.tStart = t  # local t and not account for scr refresh
                imageT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageT, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageT.status = STARTED
                imageT.setAutoDraw(True)
            
            # if imageT is active this frame...
            if imageT.status == STARTED:
                # update params
                pass
            
            # *imageL1* updates
            
            # if imageL1 is starting this frame...
            if imageL1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL1.frameNStart = frameN  # exact frame index
                imageL1.tStart = t  # local t and not account for scr refresh
                imageL1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL1, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL1.status = STARTED
                imageL1.setAutoDraw(True)
            
            # if imageL1 is active this frame...
            if imageL1.status == STARTED:
                # update params
                pass
            
            # *imageL2* updates
            
            # if imageL2 is starting this frame...
            if imageL2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL2.frameNStart = frameN  # exact frame index
                imageL2.tStart = t  # local t and not account for scr refresh
                imageL2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL2.status = STARTED
                imageL2.setAutoDraw(True)
            
            # if imageL2 is active this frame...
            if imageL2.status == STARTED:
                # update params
                pass
            
            # *imageL3* updates
            
            # if imageL3 is starting this frame...
            if imageL3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL3.frameNStart = frameN  # exact frame index
                imageL3.tStart = t  # local t and not account for scr refresh
                imageL3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL3.status = STARTED
                imageL3.setAutoDraw(True)
            
            # if imageL3 is active this frame...
            if imageL3.status == STARTED:
                # update params
                pass
            
            # *imageL4* updates
            
            # if imageL4 is starting this frame...
            if imageL4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL4.frameNStart = frameN  # exact frame index
                imageL4.tStart = t  # local t and not account for scr refresh
                imageL4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL4, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL4.status = STARTED
                imageL4.setAutoDraw(True)
            
            # if imageL4 is active this frame...
            if imageL4.status == STARTED:
                # update params
                pass
            
            # *imageL5* updates
            
            # if imageL5 is starting this frame...
            if imageL5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL5.frameNStart = frameN  # exact frame index
                imageL5.tStart = t  # local t and not account for scr refresh
                imageL5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL5, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL5.status = STARTED
                imageL5.setAutoDraw(True)
            
            # if imageL5 is active this frame...
            if imageL5.status == STARTED:
                # update params
                pass
            
            # *imageL6* updates
            
            # if imageL6 is starting this frame...
            if imageL6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL6.frameNStart = frameN  # exact frame index
                imageL6.tStart = t  # local t and not account for scr refresh
                imageL6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL6, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL6.status = STARTED
                imageL6.setAutoDraw(True)
            
            # if imageL6 is active this frame...
            if imageL6.status == STARTED:
                # update params
                pass
            
            # *imageL7* updates
            
            # if imageL7 is starting this frame...
            if imageL7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL7.frameNStart = frameN  # exact frame index
                imageL7.tStart = t  # local t and not account for scr refresh
                imageL7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL7, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL7.status = STARTED
                imageL7.setAutoDraw(True)
            
            # if imageL7 is active this frame...
            if imageL7.status == STARTED:
                # update params
                pass
            
            # *imageL8* updates
            
            # if imageL8 is starting this frame...
            if imageL8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL8.frameNStart = frameN  # exact frame index
                imageL8.tStart = t  # local t and not account for scr refresh
                imageL8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL8, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL8.status = STARTED
                imageL8.setAutoDraw(True)
            
            # if imageL8 is active this frame...
            if imageL8.status == STARTED:
                # update params
                pass
            
            # *imageL9* updates
            
            # if imageL9 is starting this frame...
            if imageL9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL9.frameNStart = frameN  # exact frame index
                imageL9.tStart = t  # local t and not account for scr refresh
                imageL9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL9, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL9.status = STARTED
                imageL9.setAutoDraw(True)
            
            # if imageL9 is active this frame...
            if imageL9.status == STARTED:
                # update params
                pass
            
            # *imageL10* updates
            
            # if imageL10 is starting this frame...
            if imageL10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL10.frameNStart = frameN  # exact frame index
                imageL10.tStart = t  # local t and not account for scr refresh
                imageL10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL10, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL10.status = STARTED
                imageL10.setAutoDraw(True)
            
            # if imageL10 is active this frame...
            if imageL10.status == STARTED:
                # update params
                pass
            
            # *imageL11* updates
            
            # if imageL11 is starting this frame...
            if imageL11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL11.frameNStart = frameN  # exact frame index
                imageL11.tStart = t  # local t and not account for scr refresh
                imageL11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL11, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL11.status = STARTED
                imageL11.setAutoDraw(True)
            
            # if imageL11 is active this frame...
            if imageL11.status == STARTED:
                # update params
                pass
            
            # *imageAperture* updates
            
            # if imageAperture is starting this frame...
            if imageAperture.status == NOT_STARTED and tThisFlip >= startApertureTime-frameTolerance:
                # keep track of start time/frame for later
                imageAperture.frameNStart = frameN  # exact frame index
                imageAperture.tStart = t  # local t and not account for scr refresh
                imageAperture.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageAperture, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageAperture.started')
                # update status
                imageAperture.status = STARTED
                imageAperture.setAutoDraw(True)
            
            # if imageAperture is active this frame...
            if imageAperture.status == STARTED:
                # update params
                imageAperture.setPos(mouselocation, log=False)
            
            # *CenterAperture* updates
            
            # if CenterAperture is starting this frame...
            if CenterAperture.status == NOT_STARTED and tThisFlip >= startApertureTime-frameTolerance:
                # keep track of start time/frame for later
                CenterAperture.frameNStart = frameN  # exact frame index
                CenterAperture.tStart = t  # local t and not account for scr refresh
                CenterAperture.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CenterAperture, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CenterAperture.started')
                # update status
                CenterAperture.status = STARTED
                CenterAperture.setAutoDraw(True)
            
            # if CenterAperture is active this frame...
            if CenterAperture.status == STARTED:
                # update params
                pass
            
            # if CenterAperture is stopping this frame...
            if CenterAperture.status == STARTED:
                if frameN >= (CenterAperture.frameNStart + 1):
                    # keep track of stop time/frame for later
                    CenterAperture.tStop = t  # not accounting for scr refresh
                    CenterAperture.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CenterAperture.stopped')
                    # update status
                    CenterAperture.status = FINISHED
                    CenterAperture.setAutoDraw(False)
            
            # *searchHint* updates
            
            # if searchHint is starting this frame...
            if searchHint.status == NOT_STARTED and tThisFlip >= searchHintStartTime-frameTolerance:
                # keep track of start time/frame for later
                searchHint.frameNStart = frameN  # exact frame index
                searchHint.tStart = t  # local t and not account for scr refresh
                searchHint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(searchHint, 'tStartRefresh')  # time at next scr refresh
                # update status
                searchHint.status = STARTED
                searchHint.setAutoDraw(True)
            
            # if searchHint is active this frame...
            if searchHint.status == STARTED:
                # update params
                pass
            
            # *key_respMain* updates
            waitOnFlip = False
            
            # if key_respMain is starting this frame...
            if key_respMain.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_respMain.frameNStart = frameN  # exact frame index
                key_respMain.tStart = t  # local t and not account for scr refresh
                key_respMain.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respMain, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_respMain.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respMain.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respMain.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respMain.status == STARTED and not waitOnFlip:
                theseKeys = key_respMain.getKeys(keyList=['a','s'], ignoreKeys=["escape"], waitRelease=False)
                _key_respMain_allKeys.extend(theseKeys)
                if len(_key_respMain_allKeys):
                    key_respMain.keys = _key_respMain_allKeys[0].name  # just the first key pressed
                    key_respMain.rt = _key_respMain_allKeys[0].rt
                    key_respMain.duration = _key_respMain_allKeys[0].duration
                    # was this correct?
                    if (key_respMain.keys == str(corrAnswer)) or (key_respMain.keys == corrAnswer):
                        key_respMain.corr = 1
                    else:
                        key_respMain.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_initial
        thisExp.addData('letterSize',lettersize);
        thisExp.addData('apertureSize',aperturesize);
        thisExp.addData('searchsize',searchsize);
        # check responses
        if key_respMain.keys in ['', [], None]:  # No response was made
            key_respMain.keys = None
            # was no response the correct answer?!
            if str(corrAnswer).lower() == 'none':
               key_respMain.corr = 1;  # correct non-response
            else:
               key_respMain.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_respMain.keys',key_respMain.keys)
        trials.addData('key_respMain.corr', key_respMain.corr)
        if key_respMain.keys != None:  # we had a response
            trials.addData('key_respMain.rt', key_respMain.rt)
            trials.addData('key_respMain.duration', key_respMain.duration)
        # Run 'End Routine' code from code_end
        mouselocation = [0, 0];
        if key_respMain.corr == 1:
            fbtext = 'correct!'
            fbcolor = 'green';
            fbdur = .2;
        else:
            fbtext = 'incorrect!'
            fbcolor = 'red';
            fbdur = 4;
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trialFeedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trialFeedback.started', globalClock.getTime())
        textFeedback.setColor(fbcolor, colorSpace='rgb')
        textFeedback.setText(fbtext)
        # keep track of which components have finished
        trialFeedbackComponents = [textFeedback]
        for thisComponent in trialFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialFeedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textFeedback* updates
            
            # if textFeedback is starting this frame...
            if textFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFeedback.frameNStart = frameN  # exact frame index
                textFeedback.tStart = t  # local t and not account for scr refresh
                textFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFeedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                textFeedback.status = STARTED
                textFeedback.setAutoDraw(True)
            
            # if textFeedback is active this frame...
            if textFeedback.status == STARTED:
                # update params
                pass
            
            # if textFeedback is stopping this frame...
            if textFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFeedback.tStartRefresh + fbdur-frameTolerance:
                    # keep track of stop time/frame for later
                    textFeedback.tStop = t  # not accounting for scr refresh
                    textFeedback.frameNStop = frameN  # exact frame index
                    # update status
                    textFeedback.status = FINISHED
                    textFeedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialFeedback" ---
        for thisComponent in trialFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trialFeedback.stopped', globalClock.getTime())
        # the Routine "trialFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "TakeABreak" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('TakeABreak.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_break
        remainingblock = 24-block;
        breakTime = 16;
          # take a break for every block
        if trial % breakTime == 0:
            continueRoutine = True;
            sumcorr = sumcorr + key_respMain.corr;
            sumrt = sumrt + key_respMain.rt;  
            avgcorr = 100*(sumcorr/breakTime);
            avgrt = sumrt/breakTime;
            if avgcorr > 90:
                accfbcolor = 'green';
                accfbtext = "Your accuracy during the last block was " + str(round(avgcorr,2)) + "%. Good job!";
            else:
                accfbcolor = 'red';
                accfbtext = "Your accuracy during the last block was only " + str(round(avgcorr,2)) + "%. Please try to be accurate.";
            if avgrt < 4.0:
                rtfbcolor = 'green';
                rtfbtext = "It took you an average of " + str(round(avgrt,2)) + "s to respond to the letter T. Good job!";
            else:
                rtfbcolor = 'red';
                rtfbtext = "It took you an average of " + str(round(avgrt,2)) + "s to respond to the letter T. Please try to be faster.";
            sumcorr = 0;
            sumrt = 0;
        else:
            sumcorr = sumcorr + key_respMain.corr;
            sumrt = sumrt + key_respMain.rt;  
            continueRoutine = False;
        # no break instruction for last block
        if remainingblock == 0:
            continueRoutine = False;
        acctext.setColor(accfbcolor, colorSpace='rgb')
        acctext.setText(accfbtext)
        rttext.setColor(rtfbcolor, colorSpace='rgb')
        rttext.setText(rtfbtext)
        textBlockRemaining.setText(remainingblock)
        key_respBreak.keys = []
        key_respBreak.rt = []
        _key_respBreak_allKeys = []
        # keep track of which components have finished
        TakeABreakComponents = [acctext, rttext, textBreak, textBlockRemaining, key_respBreak]
        for thisComponent in TakeABreakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TakeABreak" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *acctext* updates
            
            # if acctext is starting this frame...
            if acctext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                acctext.frameNStart = frameN  # exact frame index
                acctext.tStart = t  # local t and not account for scr refresh
                acctext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(acctext, 'tStartRefresh')  # time at next scr refresh
                # update status
                acctext.status = STARTED
                acctext.setAutoDraw(True)
            
            # if acctext is active this frame...
            if acctext.status == STARTED:
                # update params
                pass
            
            # *rttext* updates
            
            # if rttext is starting this frame...
            if rttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rttext.frameNStart = frameN  # exact frame index
                rttext.tStart = t  # local t and not account for scr refresh
                rttext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rttext, 'tStartRefresh')  # time at next scr refresh
                # update status
                rttext.status = STARTED
                rttext.setAutoDraw(True)
            
            # if rttext is active this frame...
            if rttext.status == STARTED:
                # update params
                pass
            
            # *textBreak* updates
            
            # if textBreak is starting this frame...
            if textBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBreak.frameNStart = frameN  # exact frame index
                textBreak.tStart = t  # local t and not account for scr refresh
                textBreak.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBreak, 'tStartRefresh')  # time at next scr refresh
                # update status
                textBreak.status = STARTED
                textBreak.setAutoDraw(True)
            
            # if textBreak is active this frame...
            if textBreak.status == STARTED:
                # update params
                pass
            
            # *textBlockRemaining* updates
            
            # if textBlockRemaining is starting this frame...
            if textBlockRemaining.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBlockRemaining.frameNStart = frameN  # exact frame index
                textBlockRemaining.tStart = t  # local t and not account for scr refresh
                textBlockRemaining.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBlockRemaining, 'tStartRefresh')  # time at next scr refresh
                # update status
                textBlockRemaining.status = STARTED
                textBlockRemaining.setAutoDraw(True)
            
            # if textBlockRemaining is active this frame...
            if textBlockRemaining.status == STARTED:
                # update params
                textBlockRemaining.setPos((0, -65), log=False)
            
            # *key_respBreak* updates
            waitOnFlip = False
            
            # if key_respBreak is starting this frame...
            if key_respBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respBreak.frameNStart = frameN  # exact frame index
                key_respBreak.tStart = t  # local t and not account for scr refresh
                key_respBreak.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respBreak, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_respBreak.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respBreak.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respBreak.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respBreak.status == STARTED and not waitOnFlip:
                theseKeys = key_respBreak.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_respBreak_allKeys.extend(theseKeys)
                if len(_key_respBreak_allKeys):
                    key_respBreak.keys = _key_respBreak_allKeys[-1].name  # just the last key pressed
                    key_respBreak.rt = _key_respBreak_allKeys[-1].rt
                    key_respBreak.duration = _key_respBreak_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TakeABreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TakeABreak" ---
        for thisComponent in TakeABreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('TakeABreak.stopped', globalClock.getTime())
        # check responses
        if key_respBreak.keys in ['', [], None]:  # No response was made
            key_respBreak.keys = None
        trials.addData('key_respBreak.keys',key_respBreak.keys)
        if key_respBreak.keys != None:  # we had a response
            trials.addData('key_respBreak.rt', key_respBreak.rt)
            trials.addData('key_respBreak.duration', key_respBreak.duration)
        # the Routine "TakeABreak" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    Testingtrials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(testingfile),
        seed=None, name='Testingtrials')
    thisExp.addLoop(Testingtrials)  # add the loop to the experiment
    thisTestingtrial = Testingtrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestingtrial.rgb)
    if thisTestingtrial != None:
        for paramName in thisTestingtrial:
            globals()[paramName] = thisTestingtrial[paramName]
    
    for thisTestingtrial in Testingtrials:
        currentLoop = Testingtrials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTestingtrial.rgb)
        if thisTestingtrial != None:
            for paramName in thisTestingtrial:
                globals()[paramName] = thisTestingtrial[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_fixinitial
        win.mouseVisible = True; # show cursor
        # fixation Hint
        if phase == 'practice':
            fixationStartTime = 4;
        else:
            fixationStartTime = 10000;
        # show mouse
        win.mouseVisible = True;
        # fixation size rescale
        fixsize = 28*expInfo['ratio_monitor2CRT'];
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        fixationPoint.setSize((fixsize, fixsize))
        fixationHint.setPos((0, hintlocation))
        # setup some python lists for storing info about the mouseintial
        mouseintial.x = []
        mouseintial.y = []
        mouseintial.leftButton = []
        mouseintial.midButton = []
        mouseintial.rightButton = []
        mouseintial.time = []
        mouseintial.clicked_name = []
        gotValidClick = False  # until a click is received
        mouseintial.mouseClock.reset()
        # keep track of which components have finished
        fixationComponents = [fixationPoint, fixationHint, mouseintial]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationPoint* updates
            
            # if fixationPoint is starting this frame...
            if fixationPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationPoint.frameNStart = frameN  # exact frame index
                fixationPoint.tStart = t  # local t and not account for scr refresh
                fixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationPoint, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationPoint.status = STARTED
                fixationPoint.setAutoDraw(True)
            
            # if fixationPoint is active this frame...
            if fixationPoint.status == STARTED:
                # update params
                pass
            
            # *fixationHint* updates
            
            # if fixationHint is starting this frame...
            if fixationHint.status == NOT_STARTED and tThisFlip >= fixationStartTime-frameTolerance:
                # keep track of start time/frame for later
                fixationHint.frameNStart = frameN  # exact frame index
                fixationHint.tStart = t  # local t and not account for scr refresh
                fixationHint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationHint, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationHint.status = STARTED
                fixationHint.setAutoDraw(True)
            
            # if fixationHint is active this frame...
            if fixationHint.status == STARTED:
                # update params
                pass
            # *mouseintial* updates
            
            # if mouseintial is starting this frame...
            if mouseintial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouseintial.frameNStart = frameN  # exact frame index
                mouseintial.tStart = t  # local t and not account for scr refresh
                mouseintial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseintial, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mouseintial.started')
                # update status
                mouseintial.status = STARTED
                prevButtonState = mouseintial.getPressed()  # if button is down already this ISN'T a new click
            if mouseintial.status == STARTED:  # only update if started and not finished!
                buttons = mouseintial.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(fixationPoint, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseintial):
                                gotValidClick = True
                                mouseintial.clicked_name.append(obj.name)
                        x, y = mouseintial.getPos()
                        mouseintial.x.append(x)
                        mouseintial.y.append(y)
                        buttons = mouseintial.getPressed()
                        mouseintial.leftButton.append(buttons[0])
                        mouseintial.midButton.append(buttons[1])
                        mouseintial.rightButton.append(buttons[2])
                        mouseintial.time.append(mouseintial.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_fixinitial
        mouselocation = [0, 0];
        thisExp.addData('fixationSize',fixsize)
        # store data for Testingtrials (TrialHandler)
        Testingtrials.addData('mouseintial.x', mouseintial.x)
        Testingtrials.addData('mouseintial.y', mouseintial.y)
        Testingtrials.addData('mouseintial.leftButton', mouseintial.leftButton)
        Testingtrials.addData('mouseintial.midButton', mouseintial.midButton)
        Testingtrials.addData('mouseintial.rightButton', mouseintial.rightButton)
        Testingtrials.addData('mouseintial.time', mouseintial.time)
        Testingtrials.addData('mouseintial.clicked_name', mouseintial.clicked_name)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "greenFixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('greenFixation.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_fixinitial_2
        win.mouseVisible = True; # show cursor
        # fixation Hint
        if phase == 'practice':
            fixationStartTime = 4;
        else:
            fixationStartTime = 10000;
        # show mouse
        win.mouseVisible = True;
        # fixation size rescale
        fixsize = 28*expInfo['ratio_monitor2CRT'];
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        fixationPoint_2.setSize((fixsize, fixsize))
        # keep track of which components have finished
        greenFixationComponents = [fixationPoint_2]
        for thisComponent in greenFixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "greenFixation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationPoint_2* updates
            
            # if fixationPoint_2 is starting this frame...
            if fixationPoint_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationPoint_2.frameNStart = frameN  # exact frame index
                fixationPoint_2.tStart = t  # local t and not account for scr refresh
                fixationPoint_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationPoint_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationPoint_2.status = STARTED
                fixationPoint_2.setAutoDraw(True)
            
            # if fixationPoint_2 is active this frame...
            if fixationPoint_2.status == STARTED:
                # update params
                pass
            
            # if fixationPoint_2 is stopping this frame...
            if fixationPoint_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationPoint_2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationPoint_2.tStop = t  # not accounting for scr refresh
                    fixationPoint_2.frameNStop = frameN  # exact frame index
                    # update status
                    fixationPoint_2.status = FINISHED
                    fixationPoint_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in greenFixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "greenFixation" ---
        for thisComponent in greenFixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('greenFixation.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_fixinitial_2
        mouselocation = [0, 0];
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.100000)
        
        # --- Prepare to start Routine "displayTestingPhase" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('displayTestingPhase.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_initial_3
        win.mouseVisible = True; # show cursor
        # initial first location to center
        mouselocation = [0, 0];
        whichframe = 0;
        # create empty list to save mouse location
        mouselocationlistx = [];
        mouselocationlisty = [];
        whichframelist = [];
        
        
        startApertureTime = 10000;
        
        
        # letter size
        lettersize = 28*expInfo['ratio_monitor2CRT'];
        # aperture size
        aperturesize = 8000*expInfo['ratio_monitor2CRT'];
        # rescale search window size
        searchsize = 482*expInfo['ratio_monitor2CRT'];
        # rescale letter location
        newtlocx = tlocx * expInfo['ratio_monitor2CRT'];
        newtlocy = tlocy * expInfo['ratio_monitor2CRT'];
        newd1x = d1x * expInfo['ratio_monitor2CRT'];
        newd1y = d1y * expInfo['ratio_monitor2CRT'];
        newd2x = d2x * expInfo['ratio_monitor2CRT'];
        newd2y = d2y * expInfo['ratio_monitor2CRT'];
        newd3x = d3x * expInfo['ratio_monitor2CRT'];
        newd3y = d3y * expInfo['ratio_monitor2CRT'];
        newd4x = d4x * expInfo['ratio_monitor2CRT'];
        newd4y = d4y * expInfo['ratio_monitor2CRT'];
        newd5x = d5x * expInfo['ratio_monitor2CRT'];
        newd5y = d5y * expInfo['ratio_monitor2CRT'];
        newd6x = d6x * expInfo['ratio_monitor2CRT'];
        newd6y = d6y * expInfo['ratio_monitor2CRT'];
        newd7x = d7x * expInfo['ratio_monitor2CRT'];
        newd7y = d7y * expInfo['ratio_monitor2CRT'];
        newd8x = d8x * expInfo['ratio_monitor2CRT'];
        newd8y = d8y * expInfo['ratio_monitor2CRT'];
        newd9x = d9x * expInfo['ratio_monitor2CRT'];
        newd9y = d9y * expInfo['ratio_monitor2CRT'];
        newd10x = d10x * expInfo['ratio_monitor2CRT'];
        newd10y = d10y * expInfo['ratio_monitor2CRT'];
        newd11x = d11x * expInfo['ratio_monitor2CRT'];
        newd11y = d11y * expInfo['ratio_monitor2CRT'];
        
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        background_3.setSize((searchsize, searchsize))
        imageT_3.setPos((newtlocx, newtlocy))
        imageT_3.setSize((lettersize, lettersize))
        imageT_3.setOri(targOrientdeg)
        imageL1_3.setPos((newd1x,newd1y))
        imageL1_3.setSize((lettersize, lettersize))
        imageL1_3.setOri(d1Orient)
        imageL2_3.setPos((newd2x,newd2y))
        imageL2_3.setSize((lettersize, lettersize))
        imageL2_3.setOri(d2Orient)
        imageL3_3.setPos((newd3x,newd3y))
        imageL3_3.setSize((lettersize, lettersize))
        imageL3_3.setOri(d3Orient)
        imageL4_3.setPos((newd4x,newd4y))
        imageL4_3.setSize((lettersize, lettersize))
        imageL4_3.setOri(d4Orient)
        imageL5_3.setPos((newd5x,newd5y))
        imageL5_3.setSize((lettersize, lettersize))
        imageL5_3.setOri(d5Orient)
        imageL6_3.setPos((newd6x,newd6y))
        imageL6_3.setSize((lettersize, lettersize))
        imageL6_3.setOri(d6Orient)
        imageL7_3.setPos((newd7x,newd7y))
        imageL7_3.setSize((lettersize, lettersize))
        imageL7_3.setOri(d7Orient)
        imageL8_3.setPos((newd8x,newd8y))
        imageL8_3.setSize((lettersize, lettersize))
        imageL8_3.setOri(d8Orient)
        imageL9_3.setPos((newd9x,newd9y))
        imageL9_3.setSize((lettersize, lettersize))
        imageL9_3.setOri(d9Orient)
        imageL10_3.setPos((newd10x,newd10y))
        imageL10_3.setSize((lettersize, lettersize))
        imageL10_3.setOri(d10Orient)
        imageL11_3.setPos((newd11x,newd11y))
        imageL11_3.setSize((lettersize, lettersize))
        imageL11_3.setOri(d11Orient)
        imageAperture_3.setSize((aperturesize, aperturesize))
        CenterAperture_3.setPos([0, 0])
        CenterAperture_3.setSize((aperturesize, aperturesize))
        key_respTesting.keys = []
        key_respTesting.rt = []
        _key_respTesting_allKeys = []
        # keep track of which components have finished
        displayTestingPhaseComponents = [background_3, imageT_3, imageL1_3, imageL2_3, imageL3_3, imageL4_3, imageL5_3, imageL6_3, imageL7_3, imageL8_3, imageL9_3, imageL10_3, imageL11_3, imageAperture_3, CenterAperture_3, key_respTesting]
        for thisComponent in displayTestingPhaseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "displayTestingPhase" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background_3* updates
            
            # if background_3 is starting this frame...
            if background_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background_3.frameNStart = frameN  # exact frame index
                background_3.tStart = t  # local t and not account for scr refresh
                background_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_3.started')
                # update status
                background_3.status = STARTED
                background_3.setAutoDraw(True)
            
            # if background_3 is active this frame...
            if background_3.status == STARTED:
                # update params
                pass
            
            # *imageT_3* updates
            
            # if imageT_3 is starting this frame...
            if imageT_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageT_3.frameNStart = frameN  # exact frame index
                imageT_3.tStart = t  # local t and not account for scr refresh
                imageT_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageT_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageT_3.status = STARTED
                imageT_3.setAutoDraw(True)
            
            # if imageT_3 is active this frame...
            if imageT_3.status == STARTED:
                # update params
                pass
            
            # *imageL1_3* updates
            
            # if imageL1_3 is starting this frame...
            if imageL1_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL1_3.frameNStart = frameN  # exact frame index
                imageL1_3.tStart = t  # local t and not account for scr refresh
                imageL1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL1_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL1_3.status = STARTED
                imageL1_3.setAutoDraw(True)
            
            # if imageL1_3 is active this frame...
            if imageL1_3.status == STARTED:
                # update params
                pass
            
            # *imageL2_3* updates
            
            # if imageL2_3 is starting this frame...
            if imageL2_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL2_3.frameNStart = frameN  # exact frame index
                imageL2_3.tStart = t  # local t and not account for scr refresh
                imageL2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL2_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL2_3.status = STARTED
                imageL2_3.setAutoDraw(True)
            
            # if imageL2_3 is active this frame...
            if imageL2_3.status == STARTED:
                # update params
                pass
            
            # *imageL3_3* updates
            
            # if imageL3_3 is starting this frame...
            if imageL3_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL3_3.frameNStart = frameN  # exact frame index
                imageL3_3.tStart = t  # local t and not account for scr refresh
                imageL3_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL3_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL3_3.status = STARTED
                imageL3_3.setAutoDraw(True)
            
            # if imageL3_3 is active this frame...
            if imageL3_3.status == STARTED:
                # update params
                pass
            
            # *imageL4_3* updates
            
            # if imageL4_3 is starting this frame...
            if imageL4_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL4_3.frameNStart = frameN  # exact frame index
                imageL4_3.tStart = t  # local t and not account for scr refresh
                imageL4_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL4_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL4_3.status = STARTED
                imageL4_3.setAutoDraw(True)
            
            # if imageL4_3 is active this frame...
            if imageL4_3.status == STARTED:
                # update params
                pass
            
            # *imageL5_3* updates
            
            # if imageL5_3 is starting this frame...
            if imageL5_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL5_3.frameNStart = frameN  # exact frame index
                imageL5_3.tStart = t  # local t and not account for scr refresh
                imageL5_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL5_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL5_3.status = STARTED
                imageL5_3.setAutoDraw(True)
            
            # if imageL5_3 is active this frame...
            if imageL5_3.status == STARTED:
                # update params
                pass
            
            # *imageL6_3* updates
            
            # if imageL6_3 is starting this frame...
            if imageL6_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL6_3.frameNStart = frameN  # exact frame index
                imageL6_3.tStart = t  # local t and not account for scr refresh
                imageL6_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL6_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL6_3.status = STARTED
                imageL6_3.setAutoDraw(True)
            
            # if imageL6_3 is active this frame...
            if imageL6_3.status == STARTED:
                # update params
                pass
            
            # *imageL7_3* updates
            
            # if imageL7_3 is starting this frame...
            if imageL7_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL7_3.frameNStart = frameN  # exact frame index
                imageL7_3.tStart = t  # local t and not account for scr refresh
                imageL7_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL7_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL7_3.status = STARTED
                imageL7_3.setAutoDraw(True)
            
            # if imageL7_3 is active this frame...
            if imageL7_3.status == STARTED:
                # update params
                pass
            
            # *imageL8_3* updates
            
            # if imageL8_3 is starting this frame...
            if imageL8_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL8_3.frameNStart = frameN  # exact frame index
                imageL8_3.tStart = t  # local t and not account for scr refresh
                imageL8_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL8_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL8_3.status = STARTED
                imageL8_3.setAutoDraw(True)
            
            # if imageL8_3 is active this frame...
            if imageL8_3.status == STARTED:
                # update params
                pass
            
            # *imageL9_3* updates
            
            # if imageL9_3 is starting this frame...
            if imageL9_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL9_3.frameNStart = frameN  # exact frame index
                imageL9_3.tStart = t  # local t and not account for scr refresh
                imageL9_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL9_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL9_3.status = STARTED
                imageL9_3.setAutoDraw(True)
            
            # if imageL9_3 is active this frame...
            if imageL9_3.status == STARTED:
                # update params
                pass
            
            # *imageL10_3* updates
            
            # if imageL10_3 is starting this frame...
            if imageL10_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL10_3.frameNStart = frameN  # exact frame index
                imageL10_3.tStart = t  # local t and not account for scr refresh
                imageL10_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL10_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL10_3.status = STARTED
                imageL10_3.setAutoDraw(True)
            
            # if imageL10_3 is active this frame...
            if imageL10_3.status == STARTED:
                # update params
                pass
            
            # *imageL11_3* updates
            
            # if imageL11_3 is starting this frame...
            if imageL11_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL11_3.frameNStart = frameN  # exact frame index
                imageL11_3.tStart = t  # local t and not account for scr refresh
                imageL11_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL11_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL11_3.status = STARTED
                imageL11_3.setAutoDraw(True)
            
            # if imageL11_3 is active this frame...
            if imageL11_3.status == STARTED:
                # update params
                pass
            
            # *imageAperture_3* updates
            
            # if imageAperture_3 is starting this frame...
            if imageAperture_3.status == NOT_STARTED and tThisFlip >= startApertureTime-frameTolerance:
                # keep track of start time/frame for later
                imageAperture_3.frameNStart = frameN  # exact frame index
                imageAperture_3.tStart = t  # local t and not account for scr refresh
                imageAperture_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageAperture_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageAperture_3.started')
                # update status
                imageAperture_3.status = STARTED
                imageAperture_3.setAutoDraw(True)
            
            # if imageAperture_3 is active this frame...
            if imageAperture_3.status == STARTED:
                # update params
                imageAperture_3.setPos(mouselocation, log=False)
            
            # *CenterAperture_3* updates
            
            # if CenterAperture_3 is starting this frame...
            if CenterAperture_3.status == NOT_STARTED and tThisFlip >= startApertureTime-frameTolerance:
                # keep track of start time/frame for later
                CenterAperture_3.frameNStart = frameN  # exact frame index
                CenterAperture_3.tStart = t  # local t and not account for scr refresh
                CenterAperture_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CenterAperture_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CenterAperture_3.started')
                # update status
                CenterAperture_3.status = STARTED
                CenterAperture_3.setAutoDraw(True)
            
            # if CenterAperture_3 is active this frame...
            if CenterAperture_3.status == STARTED:
                # update params
                pass
            
            # if CenterAperture_3 is stopping this frame...
            if CenterAperture_3.status == STARTED:
                if frameN >= (CenterAperture_3.frameNStart + 1):
                    # keep track of stop time/frame for later
                    CenterAperture_3.tStop = t  # not accounting for scr refresh
                    CenterAperture_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CenterAperture_3.stopped')
                    # update status
                    CenterAperture_3.status = FINISHED
                    CenterAperture_3.setAutoDraw(False)
            
            # *key_respTesting* updates
            waitOnFlip = False
            
            # if key_respTesting is starting this frame...
            if key_respTesting.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_respTesting.frameNStart = frameN  # exact frame index
                key_respTesting.tStart = t  # local t and not account for scr refresh
                key_respTesting.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respTesting, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_respTesting.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respTesting.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respTesting.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respTesting.status == STARTED and not waitOnFlip:
                theseKeys = key_respTesting.getKeys(keyList=['a','s'], ignoreKeys=["escape"], waitRelease=False)
                _key_respTesting_allKeys.extend(theseKeys)
                if len(_key_respTesting_allKeys):
                    key_respTesting.keys = _key_respTesting_allKeys[0].name  # just the first key pressed
                    key_respTesting.rt = _key_respTesting_allKeys[0].rt
                    key_respTesting.duration = _key_respTesting_allKeys[0].duration
                    # was this correct?
                    if (key_respTesting.keys == str(corrAnswer)) or (key_respTesting.keys == corrAnswer):
                        key_respTesting.corr = 1
                    else:
                        key_respTesting.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in displayTestingPhaseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "displayTestingPhase" ---
        for thisComponent in displayTestingPhaseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('displayTestingPhase.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_initial_3
        thisExp.addData('letterSize',lettersize);
        thisExp.addData('apertureSize',aperturesize);
        thisExp.addData('searchsize',searchsize);
        # check responses
        if key_respTesting.keys in ['', [], None]:  # No response was made
            key_respTesting.keys = None
            # was no response the correct answer?!
            if str(corrAnswer).lower() == 'none':
               key_respTesting.corr = 1;  # correct non-response
            else:
               key_respTesting.corr = 0;  # failed to respond (incorrectly)
        # store data for Testingtrials (TrialHandler)
        Testingtrials.addData('key_respTesting.keys',key_respTesting.keys)
        Testingtrials.addData('key_respTesting.corr', key_respTesting.corr)
        if key_respTesting.keys != None:  # we had a response
            Testingtrials.addData('key_respTesting.rt', key_respTesting.rt)
            Testingtrials.addData('key_respTesting.duration', key_respTesting.duration)
        # Run 'End Routine' code from code_ending
        mouselocation = [0, 0];
        if key_respTesting.corr == 1:
            fbtext = 'correct!'
            fbcolor = 'green';
            fbdur = .2;
        else:
            fbtext = 'incorrect!'
            fbcolor = 'red';
            fbdur = 4;
        # the Routine "displayTestingPhase" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trialFeedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trialFeedback.started', globalClock.getTime())
        textFeedback.setColor(fbcolor, colorSpace='rgb')
        textFeedback.setText(fbtext)
        # keep track of which components have finished
        trialFeedbackComponents = [textFeedback]
        for thisComponent in trialFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialFeedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textFeedback* updates
            
            # if textFeedback is starting this frame...
            if textFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFeedback.frameNStart = frameN  # exact frame index
                textFeedback.tStart = t  # local t and not account for scr refresh
                textFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFeedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                textFeedback.status = STARTED
                textFeedback.setAutoDraw(True)
            
            # if textFeedback is active this frame...
            if textFeedback.status == STARTED:
                # update params
                pass
            
            # if textFeedback is stopping this frame...
            if textFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFeedback.tStartRefresh + fbdur-frameTolerance:
                    # keep track of stop time/frame for later
                    textFeedback.tStop = t  # not accounting for scr refresh
                    textFeedback.frameNStop = frameN  # exact frame index
                    # update status
                    textFeedback.status = FINISHED
                    textFeedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialFeedback" ---
        for thisComponent in trialFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trialFeedback.stopped', globalClock.getTime())
        # the Routine "trialFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "TakeABreak2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('TakeABreak2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_break2
        remainingblock = 4-block;
        breakTime = 16;
          # take a break for every block
        if trial % breakTime == 0:
            continueRoutine = True;
            sumcorr = sumcorr + key_respTesting.corr;
            sumrt = sumrt + key_respTesting.rt;  
            avgcorr = 100*(sumcorr/breakTime);
            avgrt = sumrt/breakTime;
            if avgcorr > 90:
                accfbcolor = 'green';
                accfbtext = "Your accuracy during the last block was " + str(round(avgcorr,2)) + "%. Good job!";
            else:
                accfbcolor = 'red';
                accfbtext = "Your accuracy during the last block was only " + str(round(avgcorr,2)) + "%. Please try to be accurate.";
            if avgrt < 4.0:
                rtfbcolor = 'green';
                rtfbtext = "It took you an average of " + str(round(avgrt,2)) + "s to respond to the letter T. Good job!";
            else:
                rtfbcolor = 'red';
                rtfbtext = "It took you an average of " + str(round(avgrt,2)) + "s to respond to the letter T. Please try to be faster.";
            sumcorr = 0;
            sumrt = 0;
        else:
            sumcorr = sumcorr + key_respTesting.corr;
            sumrt = sumrt + key_respTesting.rt;  
            continueRoutine = False;
        # no break instruction for last block
        if remainingblock == 0:
            continueRoutine = False;
        accText.setText(accfbtext)
        rtText.setText(rtfbtext)
        textblockRemaining.setText(remainingblock)
        key_RespBreak.keys = []
        key_RespBreak.rt = []
        _key_RespBreak_allKeys = []
        # keep track of which components have finished
        TakeABreak2Components = [accText, rtText, TextBreak, textblockRemaining, key_RespBreak]
        for thisComponent in TakeABreak2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TakeABreak2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *accText* updates
            
            # if accText is starting this frame...
            if accText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                accText.frameNStart = frameN  # exact frame index
                accText.tStart = t  # local t and not account for scr refresh
                accText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(accText, 'tStartRefresh')  # time at next scr refresh
                # update status
                accText.status = STARTED
                accText.setAutoDraw(True)
            
            # if accText is active this frame...
            if accText.status == STARTED:
                # update params
                pass
            
            # *rtText* updates
            
            # if rtText is starting this frame...
            if rtText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rtText.frameNStart = frameN  # exact frame index
                rtText.tStart = t  # local t and not account for scr refresh
                rtText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rtText, 'tStartRefresh')  # time at next scr refresh
                # update status
                rtText.status = STARTED
                rtText.setAutoDraw(True)
            
            # if rtText is active this frame...
            if rtText.status == STARTED:
                # update params
                pass
            
            # *TextBreak* updates
            
            # if TextBreak is starting this frame...
            if TextBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TextBreak.frameNStart = frameN  # exact frame index
                TextBreak.tStart = t  # local t and not account for scr refresh
                TextBreak.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TextBreak, 'tStartRefresh')  # time at next scr refresh
                # update status
                TextBreak.status = STARTED
                TextBreak.setAutoDraw(True)
            
            # if TextBreak is active this frame...
            if TextBreak.status == STARTED:
                # update params
                pass
            
            # *textblockRemaining* updates
            
            # if textblockRemaining is starting this frame...
            if textblockRemaining.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textblockRemaining.frameNStart = frameN  # exact frame index
                textblockRemaining.tStart = t  # local t and not account for scr refresh
                textblockRemaining.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textblockRemaining, 'tStartRefresh')  # time at next scr refresh
                # update status
                textblockRemaining.status = STARTED
                textblockRemaining.setAutoDraw(True)
            
            # if textblockRemaining is active this frame...
            if textblockRemaining.status == STARTED:
                # update params
                textblockRemaining.setPos((0, -65), log=False)
            
            # *key_RespBreak* updates
            waitOnFlip = False
            
            # if key_RespBreak is starting this frame...
            if key_RespBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_RespBreak.frameNStart = frameN  # exact frame index
                key_RespBreak.tStart = t  # local t and not account for scr refresh
                key_RespBreak.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_RespBreak, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_RespBreak.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_RespBreak.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_RespBreak.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_RespBreak.status == STARTED and not waitOnFlip:
                theseKeys = key_RespBreak.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_RespBreak_allKeys.extend(theseKeys)
                if len(_key_RespBreak_allKeys):
                    key_RespBreak.keys = _key_RespBreak_allKeys[-1].name  # just the last key pressed
                    key_RespBreak.rt = _key_RespBreak_allKeys[-1].rt
                    key_RespBreak.duration = _key_RespBreak_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TakeABreak2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TakeABreak2" ---
        for thisComponent in TakeABreak2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('TakeABreak2.stopped', globalClock.getTime())
        # check responses
        if key_RespBreak.keys in ['', [], None]:  # No response was made
            key_RespBreak.keys = None
        Testingtrials.addData('key_RespBreak.keys',key_RespBreak.keys)
        if key_RespBreak.keys != None:  # we had a response
            Testingtrials.addData('key_RespBreak.rt', key_RespBreak.rt)
            Testingtrials.addData('key_RespBreak.duration', key_RespBreak.duration)
        # the Routine "TakeABreak2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'Testingtrials'
    
    
    # --- Prepare to start Routine "RecogQuestion" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('RecogQuestion.started', globalClock.getTime())
    key_AnswerQues.keys = []
    key_AnswerQues.rt = []
    _key_AnswerQues_allKeys = []
    # keep track of which components have finished
    RecogQuestionComponents = [Ques_text, key_AnswerQues]
    for thisComponent in RecogQuestionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RecogQuestion" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Ques_text* updates
        
        # if Ques_text is starting this frame...
        if Ques_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Ques_text.frameNStart = frameN  # exact frame index
            Ques_text.tStart = t  # local t and not account for scr refresh
            Ques_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ques_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            Ques_text.status = STARTED
            Ques_text.setAutoDraw(True)
        
        # if Ques_text is active this frame...
        if Ques_text.status == STARTED:
            # update params
            pass
        
        # *key_AnswerQues* updates
        waitOnFlip = False
        
        # if key_AnswerQues is starting this frame...
        if key_AnswerQues.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_AnswerQues.frameNStart = frameN  # exact frame index
            key_AnswerQues.tStart = t  # local t and not account for scr refresh
            key_AnswerQues.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_AnswerQues, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_AnswerQues.started')
            # update status
            key_AnswerQues.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_AnswerQues.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_AnswerQues.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_AnswerQues.status == STARTED and not waitOnFlip:
            theseKeys = key_AnswerQues.getKeys(keyList=['y','n'], ignoreKeys=["escape"], waitRelease=False)
            _key_AnswerQues_allKeys.extend(theseKeys)
            if len(_key_AnswerQues_allKeys):
                key_AnswerQues.keys = _key_AnswerQues_allKeys[0].name  # just the first key pressed
                key_AnswerQues.rt = _key_AnswerQues_allKeys[0].rt
                key_AnswerQues.duration = _key_AnswerQues_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecogQuestionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RecogQuestion" ---
    for thisComponent in RecogQuestionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('RecogQuestion.stopped', globalClock.getTime())
    # check responses
    if key_AnswerQues.keys in ['', [], None]:  # No response was made
        key_AnswerQues.keys = None
    thisExp.addData('key_AnswerQues.keys',key_AnswerQues.keys)
    if key_AnswerQues.keys != None:  # we had a response
        thisExp.addData('key_AnswerQues.rt', key_AnswerQues.rt)
        thisExp.addData('key_AnswerQues.duration', key_AnswerQues.duration)
    thisExp.nextEntry()
    # the Routine "RecogQuestion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Disclose" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Disclose.started', globalClock.getTime())
    continue_key.keys = []
    continue_key.rt = []
    _continue_key_allKeys = []
    # keep track of which components have finished
    DiscloseComponents = [Disclose_text, continue_key]
    for thisComponent in DiscloseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Disclose" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Disclose_text* updates
        
        # if Disclose_text is starting this frame...
        if Disclose_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Disclose_text.frameNStart = frameN  # exact frame index
            Disclose_text.tStart = t  # local t and not account for scr refresh
            Disclose_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Disclose_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            Disclose_text.status = STARTED
            Disclose_text.setAutoDraw(True)
        
        # if Disclose_text is active this frame...
        if Disclose_text.status == STARTED:
            # update params
            pass
        
        # *continue_key* updates
        waitOnFlip = False
        
        # if continue_key is starting this frame...
        if continue_key.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            continue_key.frameNStart = frameN  # exact frame index
            continue_key.tStart = t  # local t and not account for scr refresh
            continue_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_key, 'tStartRefresh')  # time at next scr refresh
            # update status
            continue_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if continue_key.status == STARTED and not waitOnFlip:
            theseKeys = continue_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _continue_key_allKeys.extend(theseKeys)
            if len(_continue_key_allKeys):
                continue_key.keys = _continue_key_allKeys[-1].name  # just the last key pressed
                continue_key.rt = _continue_key_allKeys[-1].rt
                continue_key.duration = _continue_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DiscloseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Disclose" ---
    for thisComponent in DiscloseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Disclose.stopped', globalClock.getTime())
    # the Routine "Disclose" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "InstrRT" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('InstrRT.started', globalClock.getTime())
    InstrRecognitionTest_key.keys = []
    InstrRecognitionTest_key.rt = []
    _InstrRecognitionTest_key_allKeys = []
    # keep track of which components have finished
    InstrRTComponents = [InstrRecognitionTest, InstrRecognitionTest_key]
    for thisComponent in InstrRTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstrRT" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrRecognitionTest* updates
        
        # if InstrRecognitionTest is starting this frame...
        if InstrRecognitionTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrRecognitionTest.frameNStart = frameN  # exact frame index
            InstrRecognitionTest.tStart = t  # local t and not account for scr refresh
            InstrRecognitionTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrRecognitionTest, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstrRecognitionTest.status = STARTED
            InstrRecognitionTest.setAutoDraw(True)
        
        # if InstrRecognitionTest is active this frame...
        if InstrRecognitionTest.status == STARTED:
            # update params
            pass
        
        # *InstrRecognitionTest_key* updates
        waitOnFlip = False
        
        # if InstrRecognitionTest_key is starting this frame...
        if InstrRecognitionTest_key.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            InstrRecognitionTest_key.frameNStart = frameN  # exact frame index
            InstrRecognitionTest_key.tStart = t  # local t and not account for scr refresh
            InstrRecognitionTest_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrRecognitionTest_key, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstrRecognitionTest_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstrRecognitionTest_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstrRecognitionTest_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstrRecognitionTest_key.status == STARTED and not waitOnFlip:
            theseKeys = InstrRecognitionTest_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _InstrRecognitionTest_key_allKeys.extend(theseKeys)
            if len(_InstrRecognitionTest_key_allKeys):
                InstrRecognitionTest_key.keys = _InstrRecognitionTest_key_allKeys[-1].name  # just the last key pressed
                InstrRecognitionTest_key.rt = _InstrRecognitionTest_key_allKeys[-1].rt
                InstrRecognitionTest_key.duration = _InstrRecognitionTest_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrRTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstrRT" ---
    for thisComponent in InstrRTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('InstrRT.stopped', globalClock.getTime())
    # the Routine "InstrRT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    RTtrials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(rtfile),
        seed=None, name='RTtrials')
    thisExp.addLoop(RTtrials)  # add the loop to the experiment
    thisRTtrial = RTtrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRTtrial.rgb)
    if thisRTtrial != None:
        for paramName in thisRTtrial:
            globals()[paramName] = thisRTtrial[paramName]
    
    for thisRTtrial in RTtrials:
        currentLoop = RTtrials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRTtrial.rgb)
        if thisRTtrial != None:
            for paramName in thisRTtrial:
                globals()[paramName] = thisRTtrial[paramName]
        
        # --- Prepare to start Routine "fixation_RT" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation_RT.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_RTfix
        win.mouseVisible = True; # show cursor
        # fixation Hint: show it through the way
        if phase == 'rt':
            fixationStartTime = 0;
        else:
            fixationStartTime = 0;
        # show mouse
        win.mouseVisible = True;
        # fixation size rescale
        fixsize = 28*expInfo['ratio_monitor2CRT'];
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        fixation_image.setSize((fixsize, fixsize))
        fixationHint_text.setPos((0, hintlocation))
        # setup some python lists for storing info about the mouseInitial
        mouseInitial.x = []
        mouseInitial.y = []
        mouseInitial.leftButton = []
        mouseInitial.midButton = []
        mouseInitial.rightButton = []
        mouseInitial.time = []
        mouseInitial.clicked_name = []
        gotValidClick = False  # until a click is received
        mouseInitial.mouseClock.reset()
        # keep track of which components have finished
        fixation_RTComponents = [fixation_image, fixationHint_text, mouseInitial]
        for thisComponent in fixation_RTComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation_RT" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_image* updates
            
            # if fixation_image is starting this frame...
            if fixation_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_image.frameNStart = frameN  # exact frame index
                fixation_image.tStart = t  # local t and not account for scr refresh
                fixation_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_image, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixation_image.status = STARTED
                fixation_image.setAutoDraw(True)
            
            # if fixation_image is active this frame...
            if fixation_image.status == STARTED:
                # update params
                pass
            
            # *fixationHint_text* updates
            
            # if fixationHint_text is starting this frame...
            if fixationHint_text.status == NOT_STARTED and tThisFlip >= fixationStartTime-frameTolerance:
                # keep track of start time/frame for later
                fixationHint_text.frameNStart = frameN  # exact frame index
                fixationHint_text.tStart = t  # local t and not account for scr refresh
                fixationHint_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationHint_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixationHint_text.status = STARTED
                fixationHint_text.setAutoDraw(True)
            
            # if fixationHint_text is active this frame...
            if fixationHint_text.status == STARTED:
                # update params
                pass
            # *mouseInitial* updates
            
            # if mouseInitial is starting this frame...
            if mouseInitial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseInitial.frameNStart = frameN  # exact frame index
                mouseInitial.tStart = t  # local t and not account for scr refresh
                mouseInitial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseInitial, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mouseInitial.started')
                # update status
                mouseInitial.status = STARTED
                prevButtonState = mouseInitial.getPressed()  # if button is down already this ISN'T a new click
            if mouseInitial.status == STARTED:  # only update if started and not finished!
                buttons = mouseInitial.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(fixationPoint, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseInitial):
                                gotValidClick = True
                                mouseInitial.clicked_name.append(obj.name)
                        x, y = mouseInitial.getPos()
                        mouseInitial.x.append(x)
                        mouseInitial.y.append(y)
                        buttons = mouseInitial.getPressed()
                        mouseInitial.leftButton.append(buttons[0])
                        mouseInitial.midButton.append(buttons[1])
                        mouseInitial.rightButton.append(buttons[2])
                        mouseInitial.time.append(mouseInitial.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_RTComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_RT" ---
        for thisComponent in fixation_RTComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation_RT.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_RTfix
        mouselocation = [0, 0];
        thisExp.addData('fixationSize',fixsize)
        # store data for RTtrials (TrialHandler)
        RTtrials.addData('mouseInitial.x', mouseInitial.x)
        RTtrials.addData('mouseInitial.y', mouseInitial.y)
        RTtrials.addData('mouseInitial.leftButton', mouseInitial.leftButton)
        RTtrials.addData('mouseInitial.midButton', mouseInitial.midButton)
        RTtrials.addData('mouseInitial.rightButton', mouseInitial.rightButton)
        RTtrials.addData('mouseInitial.time', mouseInitial.time)
        RTtrials.addData('mouseInitial.clicked_name', mouseInitial.clicked_name)
        # the Routine "fixation_RT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "displayRT" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('displayRT.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_initial_2
        win.mouseVisible = True; # show cursor
        # initial first location to center
        mouselocation = [0, 0];
        whichframe = 0;
        # create empty list to save mouse location
        mouselocationlistx = [];
        mouselocationlisty = [];
        whichframelist = [];
        
        
        startApertureTime = 10000;
        
        # search Hint for RT task
        if phase == 'rt':
            searchHintStartTime = 0;
            # first practice block (block 0)
            if block == 0:
                searchHintText = 'Indicate whether you have seen it by Y or N';
            else:
                searchHintText = 'Indicate whether you have seen it by Y or N';
        else:
            searchHintStartTime = 10000;
        
        
        # letter size
        lettersize = 28*expInfo['ratio_monitor2CRT'];
        # aperture size
        aperturesize = 8000*expInfo['ratio_monitor2CRT'];
        # rescale search window size
        searchsize = 482*expInfo['ratio_monitor2CRT'];
        # rescale letter location
        newtlocx = tlocx * expInfo['ratio_monitor2CRT'];
        newtlocy = tlocy * expInfo['ratio_monitor2CRT'];
        newd1x = d1x * expInfo['ratio_monitor2CRT'];
        newd1y = d1y * expInfo['ratio_monitor2CRT'];
        newd2x = d2x * expInfo['ratio_monitor2CRT'];
        newd2y = d2y * expInfo['ratio_monitor2CRT'];
        newd3x = d3x * expInfo['ratio_monitor2CRT'];
        newd3y = d3y * expInfo['ratio_monitor2CRT'];
        newd4x = d4x * expInfo['ratio_monitor2CRT'];
        newd4y = d4y * expInfo['ratio_monitor2CRT'];
        newd5x = d5x * expInfo['ratio_monitor2CRT'];
        newd5y = d5y * expInfo['ratio_monitor2CRT'];
        newd6x = d6x * expInfo['ratio_monitor2CRT'];
        newd6y = d6y * expInfo['ratio_monitor2CRT'];
        newd7x = d7x * expInfo['ratio_monitor2CRT'];
        newd7y = d7y * expInfo['ratio_monitor2CRT'];
        newd8x = d8x * expInfo['ratio_monitor2CRT'];
        newd8y = d8y * expInfo['ratio_monitor2CRT'];
        newd9x = d9x * expInfo['ratio_monitor2CRT'];
        newd9y = d9y * expInfo['ratio_monitor2CRT'];
        newd10x = d10x * expInfo['ratio_monitor2CRT'];
        newd10y = d10y * expInfo['ratio_monitor2CRT'];
        newd11x = d11x * expInfo['ratio_monitor2CRT'];
        newd11y = d11y * expInfo['ratio_monitor2CRT'];
        
        # hint text location rescale
        hintlocation = 255*expInfo['ratio_monitor2CRT'];
        background_2.setSize((searchsize, searchsize))
        imageT_2.setPos((newtlocx, newtlocy))
        imageT_2.setSize((lettersize, lettersize))
        imageT_2.setOri(targOrientdeg)
        imageL1_2.setPos((newd1x,newd1y))
        imageL1_2.setSize((lettersize, lettersize))
        imageL1_2.setOri(d1Orient)
        imageL2_2.setPos((newd2x,newd2y))
        imageL2_2.setSize((lettersize, lettersize))
        imageL2_2.setOri(d2Orient)
        imageL3_2.setPos((newd3x,newd3y))
        imageL3_2.setSize((lettersize, lettersize))
        imageL3_2.setOri(d3Orient)
        imageL4_2.setPos((newd4x,newd4y))
        imageL4_2.setSize((lettersize, lettersize))
        imageL4_2.setOri(d4Orient)
        imageL5_2.setPos((newd5x,newd5y))
        imageL5_2.setSize((lettersize, lettersize))
        imageL5_2.setOri(d5Orient)
        imageL6_2.setPos((newd6x,newd6y))
        imageL6_2.setSize((lettersize, lettersize))
        imageL6_2.setOri(d6Orient)
        imageL7_2.setPos((newd7x,newd7y))
        imageL7_2.setSize((lettersize, lettersize))
        imageL7_2.setOri(d7Orient)
        imageL8_2.setPos((newd8x,newd8y))
        imageL8_2.setSize((lettersize, lettersize))
        imageL8_2.setOri(d8Orient)
        imageL9_2.setPos((newd9x,newd9y))
        imageL9_2.setSize((lettersize, lettersize))
        imageL9_2.setOri(d9Orient)
        imageL10_2.setPos((newd10x,newd10y))
        imageL10_2.setSize((lettersize, lettersize))
        imageL10_2.setOri(d10Orient)
        imageL11_2.setPos((newd11x,newd11y))
        imageL11_2.setSize((lettersize, lettersize))
        imageL11_2.setOri(d11Orient)
        imageAperture_2.setSize((aperturesize, aperturesize))
        CenterAperture_2.setPos([0, 0])
        CenterAperture_2.setSize((aperturesize, aperturesize))
        key_respRT.keys = []
        key_respRT.rt = []
        _key_respRT_allKeys = []
        adjustHint_text.setPos((0, hintlocation))
        adjustHint_text.setText(searchHintText)
        # keep track of which components have finished
        displayRTComponents = [background_2, imageT_2, imageL1_2, imageL2_2, imageL3_2, imageL4_2, imageL5_2, imageL6_2, imageL7_2, imageL8_2, imageL9_2, imageL10_2, imageL11_2, imageAperture_2, CenterAperture_2, key_respRT, adjustHint_text]
        for thisComponent in displayRTComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "displayRT" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background_2* updates
            
            # if background_2 is starting this frame...
            if background_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background_2.frameNStart = frameN  # exact frame index
                background_2.tStart = t  # local t and not account for scr refresh
                background_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_2.started')
                # update status
                background_2.status = STARTED
                background_2.setAutoDraw(True)
            
            # if background_2 is active this frame...
            if background_2.status == STARTED:
                # update params
                pass
            
            # *imageT_2* updates
            
            # if imageT_2 is starting this frame...
            if imageT_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageT_2.frameNStart = frameN  # exact frame index
                imageT_2.tStart = t  # local t and not account for scr refresh
                imageT_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageT_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageT_2.status = STARTED
                imageT_2.setAutoDraw(True)
            
            # if imageT_2 is active this frame...
            if imageT_2.status == STARTED:
                # update params
                pass
            
            # *imageL1_2* updates
            
            # if imageL1_2 is starting this frame...
            if imageL1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL1_2.frameNStart = frameN  # exact frame index
                imageL1_2.tStart = t  # local t and not account for scr refresh
                imageL1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL1_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL1_2.status = STARTED
                imageL1_2.setAutoDraw(True)
            
            # if imageL1_2 is active this frame...
            if imageL1_2.status == STARTED:
                # update params
                pass
            
            # *imageL2_2* updates
            
            # if imageL2_2 is starting this frame...
            if imageL2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL2_2.frameNStart = frameN  # exact frame index
                imageL2_2.tStart = t  # local t and not account for scr refresh
                imageL2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL2_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL2_2.status = STARTED
                imageL2_2.setAutoDraw(True)
            
            # if imageL2_2 is active this frame...
            if imageL2_2.status == STARTED:
                # update params
                pass
            
            # *imageL3_2* updates
            
            # if imageL3_2 is starting this frame...
            if imageL3_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL3_2.frameNStart = frameN  # exact frame index
                imageL3_2.tStart = t  # local t and not account for scr refresh
                imageL3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL3_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL3_2.status = STARTED
                imageL3_2.setAutoDraw(True)
            
            # if imageL3_2 is active this frame...
            if imageL3_2.status == STARTED:
                # update params
                pass
            
            # *imageL4_2* updates
            
            # if imageL4_2 is starting this frame...
            if imageL4_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL4_2.frameNStart = frameN  # exact frame index
                imageL4_2.tStart = t  # local t and not account for scr refresh
                imageL4_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL4_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL4_2.status = STARTED
                imageL4_2.setAutoDraw(True)
            
            # if imageL4_2 is active this frame...
            if imageL4_2.status == STARTED:
                # update params
                pass
            
            # *imageL5_2* updates
            
            # if imageL5_2 is starting this frame...
            if imageL5_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL5_2.frameNStart = frameN  # exact frame index
                imageL5_2.tStart = t  # local t and not account for scr refresh
                imageL5_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL5_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL5_2.status = STARTED
                imageL5_2.setAutoDraw(True)
            
            # if imageL5_2 is active this frame...
            if imageL5_2.status == STARTED:
                # update params
                pass
            
            # *imageL6_2* updates
            
            # if imageL6_2 is starting this frame...
            if imageL6_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL6_2.frameNStart = frameN  # exact frame index
                imageL6_2.tStart = t  # local t and not account for scr refresh
                imageL6_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL6_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL6_2.status = STARTED
                imageL6_2.setAutoDraw(True)
            
            # if imageL6_2 is active this frame...
            if imageL6_2.status == STARTED:
                # update params
                pass
            
            # *imageL7_2* updates
            
            # if imageL7_2 is starting this frame...
            if imageL7_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL7_2.frameNStart = frameN  # exact frame index
                imageL7_2.tStart = t  # local t and not account for scr refresh
                imageL7_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL7_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL7_2.status = STARTED
                imageL7_2.setAutoDraw(True)
            
            # if imageL7_2 is active this frame...
            if imageL7_2.status == STARTED:
                # update params
                pass
            
            # *imageL8_2* updates
            
            # if imageL8_2 is starting this frame...
            if imageL8_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL8_2.frameNStart = frameN  # exact frame index
                imageL8_2.tStart = t  # local t and not account for scr refresh
                imageL8_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL8_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL8_2.status = STARTED
                imageL8_2.setAutoDraw(True)
            
            # if imageL8_2 is active this frame...
            if imageL8_2.status == STARTED:
                # update params
                pass
            
            # *imageL9_2* updates
            
            # if imageL9_2 is starting this frame...
            if imageL9_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL9_2.frameNStart = frameN  # exact frame index
                imageL9_2.tStart = t  # local t and not account for scr refresh
                imageL9_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL9_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL9_2.status = STARTED
                imageL9_2.setAutoDraw(True)
            
            # if imageL9_2 is active this frame...
            if imageL9_2.status == STARTED:
                # update params
                pass
            
            # *imageL10_2* updates
            
            # if imageL10_2 is starting this frame...
            if imageL10_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL10_2.frameNStart = frameN  # exact frame index
                imageL10_2.tStart = t  # local t and not account for scr refresh
                imageL10_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL10_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL10_2.status = STARTED
                imageL10_2.setAutoDraw(True)
            
            # if imageL10_2 is active this frame...
            if imageL10_2.status == STARTED:
                # update params
                pass
            
            # *imageL11_2* updates
            
            # if imageL11_2 is starting this frame...
            if imageL11_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageL11_2.frameNStart = frameN  # exact frame index
                imageL11_2.tStart = t  # local t and not account for scr refresh
                imageL11_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageL11_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageL11_2.status = STARTED
                imageL11_2.setAutoDraw(True)
            
            # if imageL11_2 is active this frame...
            if imageL11_2.status == STARTED:
                # update params
                pass
            
            # *imageAperture_2* updates
            
            # if imageAperture_2 is starting this frame...
            if imageAperture_2.status == NOT_STARTED and tThisFlip >= startApertureTime-frameTolerance:
                # keep track of start time/frame for later
                imageAperture_2.frameNStart = frameN  # exact frame index
                imageAperture_2.tStart = t  # local t and not account for scr refresh
                imageAperture_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageAperture_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageAperture_2.started')
                # update status
                imageAperture_2.status = STARTED
                imageAperture_2.setAutoDraw(True)
            
            # if imageAperture_2 is active this frame...
            if imageAperture_2.status == STARTED:
                # update params
                imageAperture_2.setPos(mouselocation, log=False)
            
            # *CenterAperture_2* updates
            
            # if CenterAperture_2 is starting this frame...
            if CenterAperture_2.status == NOT_STARTED and tThisFlip >= startApertureTime-frameTolerance:
                # keep track of start time/frame for later
                CenterAperture_2.frameNStart = frameN  # exact frame index
                CenterAperture_2.tStart = t  # local t and not account for scr refresh
                CenterAperture_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CenterAperture_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CenterAperture_2.started')
                # update status
                CenterAperture_2.status = STARTED
                CenterAperture_2.setAutoDraw(True)
            
            # if CenterAperture_2 is active this frame...
            if CenterAperture_2.status == STARTED:
                # update params
                pass
            
            # if CenterAperture_2 is stopping this frame...
            if CenterAperture_2.status == STARTED:
                if frameN >= (CenterAperture_2.frameNStart + 1):
                    # keep track of stop time/frame for later
                    CenterAperture_2.tStop = t  # not accounting for scr refresh
                    CenterAperture_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'CenterAperture_2.stopped')
                    # update status
                    CenterAperture_2.status = FINISHED
                    CenterAperture_2.setAutoDraw(False)
            
            # *key_respRT* updates
            waitOnFlip = False
            
            # if key_respRT is starting this frame...
            if key_respRT.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_respRT.frameNStart = frameN  # exact frame index
                key_respRT.tStart = t  # local t and not account for scr refresh
                key_respRT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respRT, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_respRT.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respRT.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respRT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respRT.status == STARTED and not waitOnFlip:
                theseKeys = key_respRT.getKeys(keyList=['y','n'], ignoreKeys=["escape"], waitRelease=False)
                _key_respRT_allKeys.extend(theseKeys)
                if len(_key_respRT_allKeys):
                    key_respRT.keys = _key_respRT_allKeys[0].name  # just the first key pressed
                    key_respRT.rt = _key_respRT_allKeys[0].rt
                    key_respRT.duration = _key_respRT_allKeys[0].duration
                    # was this correct?
                    if (key_respRT.keys == str(corrAnswer)) or (key_respRT.keys == corrAnswer):
                        key_respRT.corr = 1
                    else:
                        key_respRT.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *adjustHint_text* updates
            
            # if adjustHint_text is starting this frame...
            if adjustHint_text.status == NOT_STARTED and tThisFlip >= searchHintStartTime-frameTolerance:
                # keep track of start time/frame for later
                adjustHint_text.frameNStart = frameN  # exact frame index
                adjustHint_text.tStart = t  # local t and not account for scr refresh
                adjustHint_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(adjustHint_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                adjustHint_text.status = STARTED
                adjustHint_text.setAutoDraw(True)
            
            # if adjustHint_text is active this frame...
            if adjustHint_text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in displayRTComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "displayRT" ---
        for thisComponent in displayRTComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('displayRT.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_initial_2
        thisExp.addData('letterSize',lettersize);
        thisExp.addData('apertureSize',aperturesize);
        thisExp.addData('searchsize',searchsize);
        # check responses
        if key_respRT.keys in ['', [], None]:  # No response was made
            key_respRT.keys = None
            # was no response the correct answer?!
            if str(corrAnswer).lower() == 'none':
               key_respRT.corr = 1;  # correct non-response
            else:
               key_respRT.corr = 0;  # failed to respond (incorrectly)
        # store data for RTtrials (TrialHandler)
        RTtrials.addData('key_respRT.keys',key_respRT.keys)
        RTtrials.addData('key_respRT.corr', key_respRT.corr)
        if key_respRT.keys != None:  # we had a response
            RTtrials.addData('key_respRT.rt', key_respRT.rt)
            RTtrials.addData('key_respRT.duration', key_respRT.duration)
        # the Routine "displayRT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'RTtrials'
    
    
    # --- Prepare to start Routine "EndOfExperiment" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('EndOfExperiment.started', globalClock.getTime())
    # keep track of which components have finished
    EndOfExperimentComponents = [textEnd]
    for thisComponent in EndOfExperimentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndOfExperiment" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textEnd* updates
        
        # if textEnd is starting this frame...
        if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEnd.frameNStart = frameN  # exact frame index
            textEnd.tStart = t  # local t and not account for scr refresh
            textEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
            # update status
            textEnd.status = STARTED
            textEnd.setAutoDraw(True)
        
        # if textEnd is active this frame...
        if textEnd.status == STARTED:
            # update params
            pass
        
        # if textEnd is stopping this frame...
        if textEnd.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textEnd.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                textEnd.tStop = t  # not accounting for scr refresh
                textEnd.frameNStop = frameN  # exact frame index
                # update status
                textEnd.status = FINISHED
                textEnd.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndOfExperimentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndOfExperiment" ---
    for thisComponent in EndOfExperimentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('EndOfExperiment.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
