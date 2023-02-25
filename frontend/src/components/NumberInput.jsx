import React from "react";

//Input box component

const NumberInput = ({ label, unit, value, setter }) => {
  const onChange = (e) => setter(() => parseFloat(e.target.value));
  return (
    <div className="form-control">
      <label className="label">
        <span className="label-text">{label}</span>
      </label>
      <label className="input-group flex items-center">
        <input
          type="number"
          placeholder="Type value here"
          className="input input-bordered w-44"
          value={value}
          onChange={onChange}
        />
        <span className="flex flex-row items-center justify-center bg-gray-200 px-1 w-20 rounded-lg h-12">
          {unit}
        </span>
      </label>
    </div>
  );
};

export default NumberInput;
