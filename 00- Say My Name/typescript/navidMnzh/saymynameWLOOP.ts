// @ts-ignore: Unreachable code error
import readline from "readline-sync";

for(let i=0; true; i++){
    let name: any = readline.question("Say My Name O-O ");
    if(name == "Heisenberg"){
        console.log("You're God damn right!");
        break;
    }else if(name == 0){
        console.log("Task failed");
        break;
    }
}