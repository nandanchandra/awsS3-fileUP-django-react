import React from "react";

const Base = ({
	title = "Test Title",
	className = "bg-dark text-white p-4",
	children,
}) => {
	return (
		<div className="bg-dark">
			<div className="container-fluid">
				<div className="jumbotron bg-dark text-white text-center">
					<h2 className="display-4">{title}</h2>
				</div>
				<div className={className}>{children}</div>
			</div>
			<footer className="footer bg-dark mt-auto">
				<div className="container-fluid bg-info text-white text-center py-3">
					<h3 className="text-white">S3 IMAGE UPLOAD</h3>
					<button className="btn btn-warning btn-lg">Contact Us</button>
				</div>
			</footer>
		</div>
	);
};

export default Base;
