import PropTypes from "prop-types";

//Header of  page

const Header = ({ par }) => {
  return (
    <div className="header">
      <h1>{par}</h1>
    </div>
  );
};

Header.defaultProps = {
  par: "Range and Duration Calculator",
};

Header.propTypes = {
  title: PropTypes.string,
};
export default Header;
