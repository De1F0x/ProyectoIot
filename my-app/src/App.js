import { useState, useEffect } from "react";
import axios from 'axios';

  const Button = ({state, setState}) => {

  return(
    <button onClick={() => setState(!state)}>
      {(state)?"on":"off"}
    </button>
  )
}

function App() {
  const [ledState, setLedState] = useState(false);
  const [rfidState, setRfidState] = useState(false);
  const [servoState, setServoState] = useState(false);
  
  useEffect(() => {
    const fetchdata = async () => {
      const {data} = await axios.get("http://localhost:3004/raspberry");
      setLedState(data.led === 1);
      setRfidState(data.rfid === 1);
      setServoState(data.servo === 1);
    }
    fetchdata();
  }, []);

  return (
    <div>
      <Button state={ledState} setState={setLedState}/> 
      <Button state={rfidState} setState={setRfidState}/>
      <Button state={servoState} setState={setServoState}/>
    </div>
  );
}

export default App;
