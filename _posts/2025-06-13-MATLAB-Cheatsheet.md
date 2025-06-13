---
title: MATLAB Cheatsheet
permalink: MATLAB-Cheatsheet
date: 2025-06-13
excerpt: Whether you're just getting started or already writing symbolic math and matrix ops, this ultimate MATLAB cheatsheet walks you step-by-step from basic arrays to advanced functions — packed with practical examples, plotting tips, and hidden gems most learners miss. Ready to turbocharge your MATLAB skills?
type: Blog
categories: 
tags: 
status:
---

## 🟢 Beginner Level

### 📊 Data Types

#### 🔢 Arrays

```matlab
myArray = 1:1:10;
myArray2 = 1:2:10;
A = [1 2; 2 3];
```

#### Array Indexing

```matlab
A = [10 20; 30 40];
A(1,2);
A(3);
A(:,1);
A(2,:);
```

#### 🧩 Concatenation

```matlab
A = ones(1,4);
B = zeros(1,4);
C = [A B];
D = [A; B];
```

#### 📦 Cell Arrays

```matlab
name = {"Shuvangkar", "Swati"};
info = {"Shuvangkar", 28, [1,2,3]};
info{1};
info{3};
firstname = name{1};
firstname2 = name(1);
```

#### 🧱 Structures

```matlab
student.name = "Shuvangkar";
student.id = 1106125;
student.class = "PhD Student";
student.('name');
```

#### Arrays of Structures

```matlab
student(1).name = "Shuvangkar";
student(2).name = "Swati";
nums(1).f = 1; nums(2).f = 2;
allNums = [nums.f];
```

### 🔁 Control Flow

```matlab
for i = 1:10
    disp(i)
end

while condition
    % code
end

if condition
    % code
elseif other_condition
    % code
else
    % code
end
```

### 🖨️ Console Output

```matlab
fprintf('My name is %s\n', "Shuvangkar");
disp("Shuvangkar");
```

### 🔤 String Operations

```matlab
strcmp('a','a');
"a" == "a";
"Hello" + " World";
strcat('Good','Morning');
["Good ", "Morning"]
```

---

## 🟡 Intermediate Level

### ⚡ Vectorized Operations

```matlab
A = [1 2 3]; B = [2 4 6]; C = 10;
A + B;
A + C;
A .* B;
B ./ A;
```

### 🔎 Logical Indexing

```matlab
D = [-0.2 1.0 1.5 3.0 -1.0];
Dpositive = D(D >= 0);
```

### 🏗️ Memory Preallocation

```matlab
data = zeros(1,5);
names = cell(1,5);
```

### ⏱️ Measure Execution Time

```matlab
startTime = clock;
etime(clock, startTime);

tic;
toc;
```

### 📈 Basic Plotting

```matlab
plot(x1,y1,x2,y2,...);
plot(y);
```

### 🎨 Plotting Enhancements

```matlab
xlabel('x-axis'); ylabel('y-axis');
title('My Plot');
legend('Data 1');
grid on;
subplot(2,1,1); scatter(x,y); histogram(data);
```

### 📏 Array Dimensions

```matlab
size(A);
length(A);
numel(A);
```

### 🔧 Utility Functions

```matlab
isempty(A);
find(X==1);
unique(A);
sort(A);
mean(A);
std(A);
max(A); min(A);
any(A); all(A);
```

### 📁 File I/O

```matlab
data = readmatrix('file.csv');
writematrix(data, 'output.csv');
text = fileread('file.txt');
```

### 📊 Tables

```matlab
T = table(Name, Age);
T.Name;
T(2,:);
```

### 🔄 Loop Over Structure Fields

```matlab
fn = fieldnames(data);
for k = 1:numel(fn)
    disp(data.(fn{k}));
end
```

---

## 🔵 Advanced Level

### ∑ Symbolic Math

```matlab
sym(2)/sym(5);
syms a b c x;
f = a*x^2 + b*x + c;
syms f(x,y);
f(x,y) = x^2*y;
dfx = diff(f, x);
dfy = diff(f, y);
```

### 🧩 Matrix Operations

```matlab
inv(A);
pinv(A);
det(A);
eig(A);
rank(A);
null(A);
svd(A);
```

### 🔄 Anonymous Functions

```matlab
f = @(x) x.^2 + 1;
fminbnd(f, 0, 10);
```

### 🧪 NaN and Inf Handling

```matlab
isnan(A);
isinf(A);
fillmissing(A,'previous');
```

### 🧪 Debugging & Help

```matlab
help functionName;
doc functionName;
which functionName;
```

### 🚀 Optional Advanced Topics

- ODE solvers: `ode45`, `ode23`, `ode15s`
    
- Parallel Computing: `parfor`, `parpool`
    
- GUI: `uifigure`, `uicontrol`
    
- Classes & OOP
    
- App Designer

---
### 👋 About Me
Hi, I’m **Shuvangkar Das**, a power systems researcher with a Ph.D. in Electrical Engineering from Clarkson University. I work at the intersection of power electronics, DER, IBR, and AI — building greener, smarter, and more stable grids. Currently, I’m a Research Scientist at EPRI (though everything I share here reflects my personal experience, not my employer’s views).

Over the years, I’ve worked on real-world projects involving large scale EMT simulation and firmware development for  grid-forming and grid following inverter and reinforcement learning (RL). I also publish technical content and share hands-on insights with the goal of making complex ideas accessible to engineers and researchers.

📺 Subscribe to my [YouTube channel](https://www.youtube.com/@ShuvangkarDas), where I share tutorials, code walk-throughs, and research productivity tips.

<p><strong>Connect with me:<br></strong>
<a href="https://www.youtube.com/@ShuvangkarDas" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube">
  </a>
  <a href="https://www.linkedin.com/in/ShuvangkarDas" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin">
  </a>
  <a href="https://newsletter.shuvangkardas.com" target="_blank">
    <img src="https://img.shields.io/badge/Newsletter-Subscribe-blue?style=for-the-badge">
  </a>
  <a href="https://twitter.com/shuvangkar_das" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-Follow-blue?style=for-the-badge&logo=twitter">
  </a>
  
  <a href="https://github.com/shuvangkardas" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github">
  </a>
  <a href="https://blog.shuvangkardas.com" target="_blank">
    <img src="https://img.shields.io/badge/Blog-Read-blueviolet?style=for-the-badge">
  </a>
  
</p>

### 📚References



