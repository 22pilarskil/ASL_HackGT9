import globalBoolean from "./globalBoolean";



function UnguidedButton() {
    function changeMode() {
        let unguided = document.getElementById("Allprompts");
        
        console.log("Unguided button clicked");
        if (unguided != null && unguided != undefined) {
            console.log(unguided);
            let child = unguided.lastChild;
            unguided.removeChild(child);
        }
    }

    console.log("Unguided button created");
    return(
        <div id="unguided" className="chooseButton" onClick={changeMode}><p>UNGUIDED</p></div>
    );
}

export default UnguidedButton;
