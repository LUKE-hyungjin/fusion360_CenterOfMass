# fusion360_CenterOfMass
Fusion360 Add-in code that aligns the origin of the component to the origin of the center of mass.  
See the blog below for more information on how to use it.  
[Fusion360 center of mass](https://informluke.tistory.com/entry/Fusion360-%EC%9B%90%EC%A0%902%EC%A7%88%EB%9F%89%EC%A4%91%EC%8B%AC-Add-in)

## Installation
Go into the git hub below, download the code, and extract it. (Download ZIP)  
![image](https://user-images.githubusercontent.com/68213792/179702910-48fe9e37-48f4-4e2e-b16f-43ac19d0b616.png)

Run the following command in your shell.

##### Windows (In PowerShell)

```powershell
cd <path to fusion360_CenterOfMass-main>
Copy-Item ".\centerofmass\" -Destination "${env:APPDATA}\Autodesk\Autodesk Fusion 360\API\Scripts\" -Recurse
```

##### macOS (In bash or zsh)

```bash
cd <path to fusion360_CenterOfMass-main>
cp -r ./centerofmass "$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/"
```
Successful if added to Fusion 360 add-in as shown in the picture below  
![image](https://user-images.githubusercontent.com/68213792/179703334-6fd25639-dec5-4634-9ddd-3af51ae35c76.png)

## Can Use
* 1 component  
![image](https://user-images.githubusercontent.com/68213792/179703976-8122e3ff-4e6e-4194-a6b7-2dd5729df73b.png)
* Multiple components  
![image](https://user-images.githubusercontent.com/68213792/179704082-3d28fc43-b5e5-49da-b97d-101bc24de188.png)
* Multiple bodies within a component  
![image](https://user-images.githubusercontent.com/68213792/179704272-6645add0-3932-474f-ba38-c689f02e44e8.png)

## Can't Use
* Running on a body unit rather than on a component unit will not work
* Using Addin, hanging or moving joints and running Addin again causes problems with the center of mass origin
* Assembly does not work if there is an assembly in the assembly
## Working Picture
![image](https://user-images.githubusercontent.com/68213792/179704937-6d47c6eb-52cf-418b-8b56-3adeb9658d1b.png)
