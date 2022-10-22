import globalBoolean from "./globalBoolean";
import Prompts from "./Prompts";

function learnMode() {
    console.log("in function");
    let guided = document.getElementById("Allprompts");
    console.log("Guided button clicked");
    if (guided != null && guided != undefined ) {
        console.log(guided);
        guided = <Prompts />;
        console.log(guided);
    }
    }

function GuidedButton() {
    console.log("Guided button created");
    return(
        <div id="guided" className="chooseButton" onClick={learnMode}><p>GUIDED</p></div>
    );
}

export default GuidedButton;