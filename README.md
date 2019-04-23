# CyMOD
A Python Module to generate Compiled Binaries using cython for sharing confidential codes with customers and clients

## Getting Started

### Prerequisites
Few things required along with the libraries required to compile your codes

```
cython, python = 2.x,3.x, *corresponding C++ comipler support (Visual Studion 20YZ in windows)
```

### Running the code

1.Fork the code into your local directory<br/>
2.Decide which python version you want to use and check if corresponding support of c++ compiler is with you or not<br/>

In case of Windows, Following support is needed for different python versions:<br/>
1. Python 2.6 to 3.2 Check [Link1](https://www.microsoft.com/en-in/download/details.aspx?id=7873) [Link2](https://www.microsoft.com/en-us/download/details.aspx?id=44266)<br/>
2. Python 3.3, 3.4 Check [Link3](https://www.microsoft.com/en-in/download/details.aspx?id=23507)<br/>
3. Python 3.5 and Later Check [Link4](https://www.kunal-chowdhury.com/2015/07/download-visualstudio-2015.html#topic2)<br/>

While installing, Keep in mind to select this:  

<p align="left">
  <img src="https://cdn-images-1.medium.com/max/1600/1*Xv9TyfP4xW2DbJQKLJkWRg.png" width="250" title="hover text">
</p>

4. Make a Copy of your folder which you want to convert into compiled binary

5. Pass the path of your copied project like this:
```
python cyMOD.py <path_of_package>
```
#### Examples
Download samp_proj folder, and you can use it for a sample run
```
1. python cyMOD.py C:\Users\BIG1KOR\Desktop\samp_proj
2. python cyMOD.py C:\Users\BIG1KOR\Desktop\samp_proj -K=True
3. python cyMOD.py C:\Users\BIG1KOR\Desktop\samp_proj -K=True -A=__init__.py,main.py
```
#### For help type
```
python cyMOD.py -h
```
#### Pros/Cons
##### Pros:
1) Safe and Secure way to share code  
2) Works slightly faster than normal .py file as compilation time is saved  
3) Can be used in Win/Linux

##### Cons:
1) Generated binaries are system and python version specific

