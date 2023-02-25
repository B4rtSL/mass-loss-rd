import { useState } from "react";

const AddValues = ({ onAdd }) => {
  const [proptype, setProptype] = useState("propeller");
  const [altitude, setAltitude] = useState("");
  const [nompow, setNompow] = useState("");

  const onSubmit = (e) => {
    e.preventDefault();

    if (!(altitude && nompow)) {
      alert("Please enter values in each box");
      return;
    }

    onAdd({ proptype, altitude, nompow });
  };

  return (
    <form className="add-form" onSubmit={onSubmit}>
      <div className="form-control w-full max-w-xs">
        <label className="label">
          <span className="label-text">Select propulsion type</span>
        </label>
        <select
          className="select select-bordered w-full max-w-xs"
          value={proptype}
          name="proptype"
          id="propselect"
          onChange={(e) => setProptype(e.target.value)}
        >
          <option value="propeller">Propeller</option>
          <option value="jet">Jet</option>
        </select>
      </div>

      <div className="form-control w-full max-w-xs">
        <label className="label">
          <span className="label-text">Flight altitude</span>
          <span className="label-text-alt">Unit: m</span>
        </label>
        <input
          type="number"
          placeholder="Type value here"
          className="input input-bordered w-full max-w-xs"
          value={altitude}
          onChange={(e) => setAltitude(e.target.value)}
        />
      </div>

      <div className="form-control w-full max-w-xs">
        <label className="label">
          <span className="label-text">Nominal power</span>
          <span className="label-text-alt">Unit: kW</span>
        </label>
        <input
          type="number"
          placeholder="Type value here"
          className="input input-bordered w-full max-w-xs"
          value={nompow}
          onChange={(e) => setNompow(e.target.value)}
        />
      </div>

      <input type="submit" value="Save Inputs" className="btn" />
    </form>
  );
};

export default AddValues;
