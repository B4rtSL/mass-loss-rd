import { useState, useEffect } from "react";
import axios from "axios";
import Header from "./components/Header";
import NumberInput from "./components/NumberInput";
import Plotly from 'plotly.js-dist-min';
import "./App.css";


const App = () => {
  const [proptype, setProptype] = useState("propeller");
  const [propnumber, setPropnumber] = useState(2);
  const [startmass, setStartMass] = useState(2200);
  const [altitude, setAltitude] = useState(0);
  const [nompow, setNompow] = useState(290);
  const [efficiency, setEfficiency] = useState(0.8);
  const [fuelcons, setFuelcons] = useState(0.23);
  const [aspectratio, setAspectratio] = useState(8.7);
  const [cx0, setCx0] = useState(0.0265);
  const [area, setArea] = useState(17.02);
  const[vmin,setVmin]=useState(35);
  const[vmax,setVmax]=useState(150);
  const[Tmax, setTmax]=useState()
  const[Lmax, setLmax]=useState()
  const[VTmax, setVTmax]=useState()
  const[VLmax, setVLmax]=useState()
  const [trace, setTrace] = useState([
    {
      x: [],
      y: [],
    },
  ]);

  let layout = {
    title: {
      text: "Flight range and duration graph",
      font: {
        family: "Tahoma",
        size: 24,
      },
    },
    xaxis: {
      title: {
        text: "V [km/h]",
        font: {
          family: "Courier New, monospace",
          size: 14,
          color: "#7f7f7f",
        },
      },
    },
    yaxis: {
      title: {
        text: "",
        font: {
          family: "Courier New, monospace",
          size: 14,
          color: "#7f7f7f",
        },
      },
    },
  };

  useEffect(() => {
    Plotly.newPlot("plot", trace, layout);
  });

  const onSubmit = async (e) => {
    e.preventDefault();
    //Warning user about empty data boxes:

    // if (
    //   !(
    //     startmass &&
    //     altitude &&
    //     nompow &&
    //     efficiency &&
    //     fuelcons &&
    //     aspectratio &&
    //     cx0 &&
    //     area
    //   )
    // ) {
    //   alert("Please enter values in each box");
    //   return;
    // }
    console.log({
      proptype,
      propnumber,
      startmass,
      altitude,
      nompow,
      efficiency,
      fuelcons,
      aspectratio,
      cx0,
      area,
      vmin,
      vmax
    });
    let response = await axios.post("http://127.0.0.1:8000/", {
    altitude,
    area,
    aspectratio,
    cx0,
    efficiency,
    fuelcons,
    nompow,
    propnumber,
    proptype,
    startmass,
    vmax,
    vmin
    })
    console.log(response.data) 
    setTrace(()=> response.data)
    setTmax(()=>response.data.name)
  };  

  return (
 

    <div className="flex flex-col place-items-center">
      <div className="container">
        <Header/>
        <form className="flex flex-wrap w-full place-content-center gap-5" onSubmit={onSubmit}>

          

          <div className="form-control w-64">
            <label className="label">
              <span className="label-text">Select propulsion type</span>
            </label>
            <select
              className="select select-bordered w-full"
              value={proptype}
              name="proptype"
              id="propselect"
              onChange={(e) => setProptype(e.target.value)}
            >
              <option value="propeller">Propeller</option>
              <option value="jet">Jet</option>
            </select>
          </div>

          <NumberInput
            label="Number of propellers"
            unit="none"
            value={propnumber}
            setter={setPropnumber}
          />

          <NumberInput
            label="Starting mass"
            unit="kg"
            value={startmass}
            setter={setStartMass}
          />

          <NumberInput
            label="Flight altitude"
            unit="m"
            value={altitude}
            setter={setAltitude}
          />

          <NumberInput
            label="Nominal power"
            unit="kW"
            value={nompow}
            setter={setNompow}
          />

          <NumberInput
            label="Propeller efficiency ratio"
            unit="none"
            value={efficiency}
            setter={setEfficiency}
          />

          <NumberInput
            label="Specific fuel consumption"
            unit="kg/kW/h"
            value={fuelcons}
            setter={setFuelcons}
          />

          <NumberInput
            label="Effective Aspect Ratio"
            unit="none"
            value={aspectratio}
            setter={setAspectratio}
          />

          <NumberInput
            className="w-full"
            label="Minimal drag coefficient"
            unit="none"
            value={cx0}
            setter={setCx0}
          />

          <NumberInput
            label="Wing area"
            unit="m^2"
            value={area}
            setter={setArea}
          />

          <NumberInput
            label="Minimal velocity"
            unit="m/s"
            value={vmin}
            setter={setVmin}
          />

          <NumberInput
            label="Maximal velocity"
            unit="m/s"
            value={vmax}
            setter={setVmax}
          />
          <div className="break"></div>
          <input type="submit" value="Save Inputs" className="btn flex items-center justify-center align-self-center"  />
        </form>
      </div>

      <div className="flex justify-center w-1/2 p-2">
        <div id="plot" ></div>               
      </div>

      <div className="overflow-x-auto">
        <table className="table w-full">
          
          <thead>
            <tr>
              <th></th>
              <th>{Tmax}</th>
              <th>Velocity</th>
            </tr>
          </thead>
          <tbody>
            
            <tr>
              <th>Max Time [unit]</th>
              <td>y</td>
              <td>x [km/h]</td>
              
            </tr>
            
            <tr>
              <th>Max Range [unit]</th>
              <td>y</td>
              <td>x [km/h]</td>
              
            </tr>
            
          </tbody>
        </table>
      </div>

    </div>
 
  );
};

export default App;
