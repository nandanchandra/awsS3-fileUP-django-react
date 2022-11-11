import ImageHelper from "./helper/imageHelper";

const Card = ({ product, setReload = (f) => f }) => {
	const cartTitle = product ? product.title : "Not Available";

	return (
		<div className="card text-white bg-dark border border-info ">
			<div className="card-header lead">{cartTitle}</div>
			<div className="card-body">
				<ImageHelper product={product} />
			</div>
		</div>
	);
};

export default Card;
