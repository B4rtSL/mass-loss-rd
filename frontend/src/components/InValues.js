const InValues = ({ values }) => {
  return (
    <>
      {values.map((values) => (
        <div className="form-control w-full max-w-xs" key={values.id}>
          <label className="label">
            <span className="label-text">{values.text}</span>
            <span className="label-text-alt">Unit: {values.unit}</span>
          </label>
          <input
            type="number"
            placeholder="Type value here..."
            className="input input-bordered w-full max-w-xs"
          />
          <label className="label">
            <span className="label-text-alt">Decimal separator is "."</span>
          </label>
        </div>
      ))}
    </>
  );
};
export default InValues;
