import { API } from "../../backend";

export const getProducts = () => {
	return fetch(`${API}image/aws/`, { method: "GET" })
		.then((response) => {
			return response.json();
		})
		.catch((err) => console.log(err));
};
