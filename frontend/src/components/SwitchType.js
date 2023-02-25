import { useState } from "react";

const SwitchType = () => {
  const [proptype, setProptype] = useState("propeller");

  const onSubmit = (e) => {
    e.preventDefault();
    console.log(proptype);
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
      <input type="submit" value="Save propulsion type" className="btn" />
    </form>
  );
};

export default SwitchType;
