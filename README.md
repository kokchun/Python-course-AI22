# Programmering med Python (2021)

This is a fundamental Python course with focus of learning important programming concepts in order to solve various problems by writing Python programs. All lecture codes can be found in the course [Github repo][ghr].

[ghr]: https://github.com/kokchun/Programmering-med-Python-21


## Schedule

For detailed schedule [click here][time_sched]

[time_sched]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/ScheduleAI21.md

|       Week       | Content                                                                    |
| :--------------: | -------------------------------------------------------------------------- |
| [34][w1] | installation, git, vscode, variables, I/O, if, while, lab 1                |
| [35][w2] | for, lists, random, matplotlib, pipenv                                     |
| [36][w3] | strings, functions, exception handling, lab 2                              |
| [37][w4] | file handling, dictionary, lab 2                                           |
| [38][w5] | OOP: class, object, attributes, properties, docstring, polymorphism, lab 3 |
| [39][w6] | OOP: inheritance, unit testing, modules, lab 3                             |
| [40][w7] | lab3, repetition                                                           |
| [41][w8] | written exam                                                               |

[w1]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Weekly_resources/Week34.md
[w2]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Weekly_resources/Week35.md
[w3]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Weekly_resources/Week36.md
[w4]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Weekly_resources/Week37.md
[w5]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Weekly_resources/Week38.md
[w6]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Weekly_resources/Week39.md
[w7]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Weekly_resources/Week40.md
[w8]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Weekly_resources/Week41.md

## Resources

Many exercises and lecture materials are in form of Jupyter notebooks with **.ipynb** extensions. Sometimes GitHub may not load them correctly for preview, then you can use [Open in Colab][colab_addon], which is an addon in Chrome to open the notebook in Colab. Alternatively, you can go to [jupyter nbviewer][nbviewer], and paste the link to the notebook for previewing. When working with exercises it is important that you create your own notebooks (.ipynb) or script files (.py).

[nbviewer]: https://nbviewer.jupyter.org/
[colab_addon]: https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo?hl=sv

When installing softwares, unless anything else is stated in the resources, just click next.

[Check resources](https://github.com/kokchun/Programmering-med-Python-21/tree/main/Weekly_resources)

<!--
<details open>

<summary id = "wesek1"><b>Week 34</b></summary>

Setup :wrench:

- Download newest version of [Python here][pyt] and install it. Important to check :ballot_box_with_check: **add to path** in the installation. Make sure to have only **one** version of Python installed.

[pyt]: https://www.python.org/downloads/

- Download [Visual Studio Code here][vscode] and install it.

[vscode]: https://code.visualstudio.com/

- Download [git here][git] and install it.

[git]: https://git-scm.com/

- Create an account on [GitHub][github].

[github]: https://github.com/

Video guides :video_camera:
- Learn [Git and GitHub][git_tutorial] for version control and file storage

[git_tutorial]: https://www.youtube.com/watch?v=USjZcfj8yxE

- When entering the commands `python` or `pip` in command prompt or terminal and there is an error :x:, you need to set the path manually
  - set path in [Windows][windows_path]
  - set path in [Mac/Linux][mac_path]

[windows_path]: https://www.youtube.com/watch?v=dj5oOPaeIqI
[mac_path]: https://www.youtube.com/watch?v=PUIE7CPANfo

- Learn [variables][variables] to store data
- Learn [input][input] to let user input to the program
- Learn [while statement][while_video] to repeat code with given condition

[while_video]: https://www.youtube.com/watch?v=6TEGxJXLAWQ
[variables]: https://www.youtube.com/watch?v=Z1Yd7upQsXY&t=470s
[input]: https://www.youtube.com/watch?v=4OX49nLNPEE

Theory :book:
- [Github repo tutorial][git_repo_tutorial]
- [Variables - w3schools][w3var]
- [Input - w3schools][w3input]
- [while - w3schools][w3while]

[git_repo_tutorial]: https://github.com/niklas-hjelm/Programmering-med-C-Sharp/blob/main/assets/newRepo.md
[w3while]: https://www.w3schools.com/python/python_while_loops.asp
[w3var]: https://www.w3schools.com/python/python_variables.asp
[w3input]: https://www.w3schools.com/python/python_user_input.asp

Lecture notes :mortar_board:
- [Input-output, variables](https://github.com/kokchun/Programmering-med-Python-21/blob/main/Lectures/L0-input-output.ipynb)
- [if-statement](https://github.com/kokchun/Programmering-med-Python-21/blob/main/Lectures/L1-if-statements.ipynb)
- [while loop](https://github.com/kokchun/Programmering-med-Python-21/blob/main/Lectures/L2-while-statement.ipynb)

Exercises :running:
- [Count with Python][exercise_count]
- [if statement][exercise_if]
- [while statement][exercise_while]

[exercise_count]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/00-Count-with-Python-exercise.ipynb
[exercise_if]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/01-if-statement-exercise.ipynb
[exercise_while]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/02-while-statement-exercise.ipynb

Lab 1
- Deadline friday week 34  :hourglass_flowing_sand:


</details>


[if_else]: https://www.youtube.com/watch?v=AWek49wXGzI&t=155s

<details open>
 -->
<!-- <summary id = "week2"><b >Week 35</b></summary>

Video guides :video_camera:
- Learn [for statement][for_video] to efficiently repeat code
- Learn [lists][lists_video] for organizing data
- Learn [list comprehension][list_comp_vid] for efficient and clean code
- Learn [pipenv][pipenv] to manage packages and environments
- Learn [matplotlib][matplot_video] to plot graphs

[matplot_video]: https://www.youtube.com/watch?v=nzKy9GY12yo

[for_video]: https://www.youtube.com/watch?v=OnDr4J2UXSA

[pipenv]: https://www.youtube.com/watch?v=6Qmnh5C4Pmo

[lists_video]: https://www.youtube.com/watch?v=ohCDWZgNIU0&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=14

[list_comp_vid]: https://www.youtube.com/watch?v=AhSvKGTh28Q&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=22


Theory
- [pipenv - Real Python][real_pipenv]
- [for - w3schools][w3for]
- [list - w3schools][w3list]
- [matplotlib - w3schools][w3matplot]

[w3matplot]: https://www.w3schools.com/python/matplotlib_intro.asp
[w3list]: https://www.w3schools.com/python/python_lists.asp
[w3for]: https://www.w3schools.com/python/python_for_loops.asp
[real_pipenv]: https://realpython.com/pipenv-guide/

Lecture notes :mortar_board:
- [for loop](https://github.com/kokchun/Programmering-med-Python-21/blob/main/Lectures/L3-for-statement.ipynb)
- [lists](https://github.com/kokchun/Programmering-med-Python-21/blob/main/Lectures/L4-lists.ipynb)

Exercises :running:
- [for statement][exercise_for]
- [list][exercise_list]

[exercise_for]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/03-for-statement-exercise.ipynb

[exercise_list]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/04-list-exercise.ipynb

</details>


<details open>

<summary id = "week3"><b >Week 36</b></summary>

Video guides :video_camera:
- Learn [functions][func_vid] to organize and reuse code
- Learn [strings][string_vid] to work with text
- Learn [f-string][f_string_vid] to nicely format strings

[func_vid]: https://www.youtube.com/watch?v=NE97ylAnrz4
[string_vid]: https://www.youtube.com/watch?v=k9TUPpGqYTo
[f_string_vid]: https://www.youtube.com/watch?v=nghuHvKLhJA

Theory :book:
- [strings - w3schools][w3str]
- [functions - w3schools][w3func]

[w3str]: https://www.w3schools.com/python/python_strings.asp
[w3func]: https://www.w3schools.com/python/python_functions.asp

Exercises :running:
- [strings][str_exercise]
- [functions][func_exercise]

[str_exercise]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/05-strings-exercise.ipynb

[func_exercise]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/06-functions-exericse.ipynb

Lab 2
- deadline week 37 friday :hourglass_flowing_sand:

</details> -->

<!-- <details open>

<summary id = "week4"><b >Week 37</b></summary>

Video guides :video_camera:
- Learn [exceptions][except_vid] for error handling
- Learn [files][file_vid] for reading and writing to files
- Learn [dictionary][dict_vid] for storing and accessing data using key-value pairs


[except_vid]: https://www.youtube.com/watch?v=nlCKrKGHSSk&t=1s
[file_vid]: https://www.youtube.com/watch?v=4mX0uPQFLDU
[dict_vid]: https://www.youtube.com/watch?v=XCcpzWs-CI4

Theory :book:
- [exception - w3schools][w3except]
- [file handling - real python][real_files]
- [dictionary - w3schools][w3dict]

[w3dict]: https://www.w3schools.com/python/python_dictionaries.asp
[w3except]: https://www.w3schools.com/python/python_try_except.asp
[real_files]: https://realpython.com/read-write-files-python/

Exercises :running:
- [exception][except_exer]
- [file handling][file_exer]
- [dictionary][dict_exer]

[except_exer]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/07-exception-exercise.ipynb

[file_exer]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/08-file-handling.ipynb

[dict_exer]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/09-dictionary-exercises.ipynb

Lab 2
- deadline week 37 friday :hourglass_flowing_sand: -->

<!-- </details>


<details open>

<summary id = "week5"><b >Week 38</b></summary>

Video guides :video_camera:
- Learn [Classes and objects][class_vid] for code organization and reusability
- Continue on [classes and objects][class_vid2]

[class_vid]: https://www.youtube.com/watch?v=wfcWRAxRVBA
[class_vid2]: https://www.youtube.com/watch?v=WOwi0h_-dfA


Theory :book:
- [OOP - Real Python][OOP_real]
- [OOP - w3schools][w3OOP]

[OOP_real]: https://realpython.com/python3-object-oriented-programming/
[w3OOP]: https://www.w3schools.com/python/python_classes.asp

Exercises :running:

- [OOP][OOP_exer]

[OOP_exer]: https://github.com/kokchun/Programmering-med-Python-21/blob/main/Exercises/10-OOP-basic-exercise.ipynb

</details> -->

<!-- <details>

<summary id = "week6"><b >Week 39</b></summary>

Video guides :video_camera:

Theory :book:

Exercises :running:

</details> -->

<!-- <details>

<summary id = "week7"><b >Week 40</b></summary>

Video guides :video_camera:

Theory :book:

Exercises :running:

</details>

<details>

<summary id = "week8"><b >Week 41</b></summary>

Exam

</details> -->
