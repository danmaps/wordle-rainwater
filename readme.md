# [Wordle Rainwater Trapping](https://danmaps.github.io/wordle-rainwater/)
This is a fun project that combines [Wordle](https://www.nytimes.com/games/wordle/index.html) and the [rainwater trapping problem](https://leetcode.com/problems/trapping-rain-water/). I wanted to learn [pyscript](https://docs.pyscript.net/latest/tutorials/getting-started.html), so I made this. 

## What is Wordle?
In case you've been living under a rock, Wordle is a popular word game where you have to guess a five-letter word in six tries. You get feedback on each guess based on how many letters are correct and in the right position (green), correct but in the wrong position (yellow), or incorrect (gray).

## What is rainwater trapping?
Rainwater trapping is a classic coding problem where you have to find the maximum amount of water that can be trapped within a given set of bars where each bar’s width is 1 unit. For example:

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

![rainwatertrap](https://user-images.githubusercontent.com/61806500/190046292-fc841270-b48c-4834-a09a-67e72cb42dc3.png)

<b>Input</b>: height = `[0,1,0,2,1,0,1,3,2,1,2,1]`<br>
<b>Output</b>: `6`<br>
<b>Explanation</b>: The above elevation map (black section) is represented by array `[0,1,0,2,1,0,1,3,2,1,2,1]`. In this case, `6` units of rain water (blue section) are being trapped.<br>


## How does this project combine Wordle and rainwater trapping?
After looking at wordle scores, _every single day_, I started to wonder if/how I could compute how much rainwater would be trapped by this as an "elevation map". I also wondered how easy it would be to put this on a webpage with pyscript. Turns out, pretty easy!

Given the following wordle score:
```
⬛⬛⬛⬛⬛
⬛⬛⬛⬛🟩
🟩⬛⬛⬛🟩
🟩⬛🟩⬛🟩
🟩⬛🟩⬛🟩
```

we can imagine  the following elevation map and determine that it "traps" 7 units of rain water.
```
[3, 0, 2, 0, 4]

⬛⬛⬛⬛⬛
⬛⬛⬛⬛🟩
🟩🟦🟦🟦🟩
🟩🟦🟩🟦🟩
🟩🟦🟩🟦🟩
```
## How does it work?
This project uses pyscript to create a very simple web app that takes a Wordle score as input and displays the corresponding elevation map and water count as output. It also uses some logic from [this article](https://www.techiedelight.com/trapping-rain-water-within-given-set-bars/) to solve the rainwater trapping problem.

Play with it [here](https://danmaps.github.io/wordle-rainwater/).

## Thanks
* https://docs.pyscript.net/latest/tutorials/getting-started.html
* https://leetcode.com/problems/trapping-rain-water/
* https://jeff.glass/post/pyscript-why-create-proxy/
* https://www.nytimes.com/games/wordle/index.html
* https://www.techiedelight.com/trapping-rain-water-within-given-set-bars/
* https://github.com/tarmo888/Wordle2Townscaper