const signUpButton = document.getElementById('signUp1');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');


signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});




const x=document.getElementById("login");
const y=document.getElementById("signup");
const z=document.getElementById("btn");
const changetext = document.getElementById('login1');


function register()
{
	x.style.left="-400px";
	y.style.left="100px";
	z.style.left="112.5px";
	z.style.color='white';
		changetext.innerText='CREATE ACCOUNT'




}


function login()
{
	x.style.left="100px";
	y.style.left="500px";
	z.style.left="0px";
	changetext.innerText='LOGIN'
		z.style.color='white';


}