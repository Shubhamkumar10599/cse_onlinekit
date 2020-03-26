const openNav= () =>{
    
    document.getElementById('sidebarMenu').style.width="250px";
    document.getElementById('open').style.display='none';
    document.getElementById('close').style.display='block';
}

const closeNav= () =>{

    document.getElementById('sidebarMenu').style.width="0";
    document.getElementById('open').style.display='block';
    document.getElementById('close').style.display='none';

}
