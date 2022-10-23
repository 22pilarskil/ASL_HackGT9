import handImage from "../assets/handimage.jpg";
function Home() {
    return (
        <div id="HomeComponent">
        <h1 className="main">Speak with your hands.</h1>
        <div id="home">
            <div id="T">
                <p style={{color:"black"}} className="right pHome">In a society moving towards inclusivity, our app is designed to help diversify communication to support those who are deaf or mute. This web application offers a convenient, interactive approach to practicing letters in sign language. Explore the practice page to learn and practice signs, or select the translate page to use sign-to-text functionality.</p>
                <p style={{color:"black"}} className="right pHome">Whether you learn the entire alphabet or just the letters in your name, exposure to sign language is important to embrace diverse forms of communication!</p>

            </div>
            <div id="imgH">
                <img src={handImage} className="rotate homeimg"/>
            </div>
        </div>
        </div>
    );
}

export default Home;