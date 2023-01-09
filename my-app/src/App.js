import { useState, useEffect } from "react";
import axios from 'axios';
import "./style.css";
import led from './images/diodo-led.png';
import dist from './images/raspberry-pi.png';
import hum from './images/raspberry.png';


const NavBar = () => {
  return (
    <nav className="navbar navbar-expand-sm bg-dark navbar-dark d-flex justify-content-between">
      <div className="p-2"><span id="subtitle">Proyecto IoT</span></div>
      <div className="p-2"><span id="subtitle">DIEGO, BIDATZ y MIKEL</span></div>
    </nav>
  );
}

const Container = ({ ledState, setLedState, rfidState, setRfidState, servoState, setServoState }) => {
  const changeState = async (buttonType) => {
    const newState = {
      raspberry: {
        bombilla: buttonType === "bombilla" ? !ledState : ledState,
        sonido: buttonType === "sonido" ? !rfidState : rfidState,
        servo: buttonType === "servo" ? !servoState : servoState,
      }
    };

    if (buttonType === "bombilla") setLedState(!ledState);
    else if (buttonType === "sonido") setRfidState(!rfidState);
    else if (buttonType === "servo") setServoState(!servoState);

    await axios
      .post("http://192.168.1.130:4000/conf", newState);
  };

  return (
    <div className="container">
      <div className="led_cont">
        <div className="led_txt">
          <p>Sensor de luz</p>
        </div>
        <div className="led_btn">
          <button onClick={() => changeState("bombilla")}>
            {(ledState) ? "on" : "off"}
          </button>
        </div>
        <div className="led_img">
          <img src={led} height="35" width="35" alt="imagen-led" />
        </div>
      </div>

      <div className="rfid_cont">
        <div className="rfid_txt">
          <p>Sensor RFID</p>
        </div>
        <div className="rfid_btn">
          <button onClick={() => changeState("sonido")}>
            {(rfidState) ? "on" : "off"}
          </button>
        </div>
        <div className="rfid_img">
          <img src={dist} height="35" width="35" alt="imagen-rfid" />
        </div>
      </div>

      <div className="servo_cont">
        <div className="servo_txt">
          <p>Sensor servo</p>
        </div>
        <div className="servo_btn">
          <button onClick={() => changeState("servo")}>
            {(servoState) ? "on" : "off"}
          </button>
        </div>
        <div className="servo_img">
          <img src={hum} height="35" width="35" alt="imagen-servo" />
        </div>
      </div>

    </div>
  );
}

const Footer = () => {
  return (
    <footer>
      <div className="img_container">
        <p>Proyecto Final IoT</p>
      </div>
    </footer>

  );
}

function App() {
  const [ledState, setLedState] = useState(false);
  const [rfidState, setRfidState] = useState(false);
  const [servoState, setServoState] = useState(false);

  useEffect(() => {
    const fetchdata = async () => {
      const { data } = await axios.get("http://192.168.1.130:4000/conf");
      setLedState(data.led === 1);
      setRfidState(data.rfid === 1);
      setServoState(data.servo === 1);
    }
    fetchdata();
  }, []);

  return (
    <>
      <body>
        <NavBar />
        <main>
          <Container
            ledState={ledState} setLedState={setLedState}
            rfidState={rfidState} setRfidState={setRfidState}
            servoState={servoState} setServoState={setServoState}
          />
        </main>
      </body>
      <Footer />
    </>
  );
}

export default App;