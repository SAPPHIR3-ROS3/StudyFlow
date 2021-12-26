<div align="center">
    <img alt = "Logo" height = "200" src = "Icon.png">
    <h1>StudyFlow</h1>
    <a href="https://github.com/SAPPHIR3-ROS3/StudyFlow">
        <img alt="GitHub license" src="https://img.shields.io/github/license/SAPPHIR3-ROS3/StudyFlow?label=Licence">
    </a>
    <img alt="Platforms" src = "https://img.shields.io/badge/platform-win--64%20%7C%20linux--64%20%7C%20osx%20%7C%20macOS-blue">
    <a href="https://www.codefactor.io/repository/github/sapphir3-ros3/studyflow">
        <img src="https://www.codefactor.io/repository/github/sapphir3-ros3/studyflow/badge" alt="CodeFactor" />
        </a>
    <img alt="technology" src = "https://img.shields.io/badge/language-python%203-blue"/>
</div>
<p align = "center">
    StudyFlow is a simple timer that follows your flow built on <a href ="https://www.python.org/">Python</a><br>
    <img alt = "Live Demo" src = "http://g.recordit.co/ixjMho2cGS.gif"/>
</p>

## How to Install
### Automatic
* download the executable for your system
* open the app
### Manual
* download <a href ="https://www.python.org/">Python</a><br>
* open the terminal
```sh
pip install PySide6
git clone https://github.com/SAPPHIR3-ROS3/StudyFlow.git
cd StudyFlow
python StudyFlow.py
```

## How to Use
once StudyFlow started you need to set the following entries (no particular order)
* Min. Time (Minutes)
* Max. Time (Minutes)
* Break Time (Minutes)
* Over Time (Minutes)
* Sessions (Quantity)
<div>
after filling all the entries you need to press start (flag) button in order to start the timer. while the timer is running you can always pause, but you can't skip to break if you have not reached the minimum time elapsed<br>
if you passed the minimum time  from the start of the timer you can take a break pressing the skip (fast forward) button<br><br>
NOTE<br>
if you continue to study even after the maximum time set, you will go in over time NOT on break. If you set the over time to 0 you will go on break
</div>
<br>

## Credits
* <a href = "https://www.youtube.com/watch?v=bUjGZJIgse0&ab_channel=JoshChen">Video</a> I took inspiration from
<br>

## Licence

The MIT License (MIT) 2021 - <a href = "https://github.com/SAPPHIR3-ROS3">Patrizio Simone Onida</a>. Please have a look at the <a href = "LICENSE">licence</a> for more details.
