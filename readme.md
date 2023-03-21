I wanted to learn pyscript, so I made this. It seems to work!

## What?
See the following [classic leetcode problem](https://leetcode.com/problems/trapping-rain-water/):

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

![rainwatertrap](https://user-images.githubusercontent.com/61806500/190046292-fc841270-b48c-4834-a09a-67e72cb42dc3.png)

<b>Input</b>: height = `[0,1,0,2,1,0,1,3,2,1,2,1]`<br>
<b>Output</b>: `6`<br>
<b>Explanation</b>: The above elevation map (black section) is represented by array `[0,1,0,2,1,0,1,3,2,1,2,1]`. In this case, `6` units of rain water (blue section) are being trapped.<br>


## What does this have to do with Wordle?
After looking at wordle scores, _every single day_, I started to wonder if/how I could compute how much rainwater would be trapped by this as an "elevation map". I also wondered how easy it would be to put this on a webpage with pyscript. Turns out, pretty easy!

Given the following wordle score:
```
Your wordle score ?/6
   
⬛⬛⬛⬛⬛
⬛⬛⬛⬛🟩
🟩⬛⬛⬛🟩
🟩⬛🟩⬛🟩
🟩⬛🟩⬛🟩
```


we can imagine  the following elevation map and determine that it "traps" 7 units of rain water.
```
[3, 0, 2, 0, 4]
7 water
⬛⬛⬛⬛⬛
⬛⬛⬛⬛🟩
🟩🟦🟦🟦🟩
🟩🟦🟩🟦🟩
🟩🟦🟩🟦🟩
```
neat!

## Thanks
* https://docs.pyscript.net/latest/tutorials/getting-started.html
* https://leetcode.com/problems/trapping-rain-water/
* https://jeff.glass/post/pyscript-why-create-proxy/
* https://www.nytimes.com/games/wordle/index.html
* https://www.techiedelight.com/trapping-rain-water-within-given-set-bars/
* https://github.com/tarmo888/Wordle2Townscaper