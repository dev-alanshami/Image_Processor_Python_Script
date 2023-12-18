# Image Processor Python Script

### A Processing Programs that performs image processing on an image of 256x256 pixles, in which a user chooses.

![](https://github.com/dev-alanshami/Image_Processor_Python_Script/blob/main/assets/demo.gif)

### The program check for requirments before running the program (C compiler, SWIpl, matlab, Haskell Compiler).

### Steps
1. The first step, python script makes an API call locally to a matlab program where it turns the image to a binary file.
2. Then, C program takes the output of matlab and and reverse the image colors by modifying the binary file.
3. Haskell code also takes the binary file and modify it to flip the image colors.
4. Then, Prolog code rotate the original image to a 90 degrees.
5. Finally, another matlab code takes the output of all of them and displays the results.

![Watch the video Demo](https://youtu.be/2MSGil_I3-w)
