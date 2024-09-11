import { goto } from "$app/navigation";
import { PUBLIC_SERVER } from "$env/static/public";
import { error } from "@sveltejs/kit";
import { account } from "$lib/store";
import { firebaseAuth } from "$lib/configs/firebase";

export const fetchData = async (url: string, requestInit?: RequestInit) => {
	if (!sessionStorage.getItem("token")) return error(400, "No token");

	const token = sessionStorage.getItem("token") || "";

	if (token === "") throw error(400, "No token");

	if (!requestInit) requestInit = {};

	requestInit.headers = requestInit.headers
		? {
				...requestInit.headers,
				"Content-Type": "application/JSON",
				Authorization: "Bearer " + token
			}
		: {
				"Content-Type": "application/JSON",
				Authorization: "Bearer " + token
			};

	const response = await fetch(url, requestInit);

	await handleError(response);

	return response;
};

const handleError = async (response: Response) => {
	if (!response.ok) {
		const errorBody = await response.text();
		console.error("Error :" + errorBody);
		if (response.status === 401) logout();
		throw error(response.status, response.statusText);
	}
};

export const logout = async () => {
	await firebaseAuth.signOut();

	clearSessionStorage();

	// const requestInit: RequestInit = {
	// 	method: "DELETE"
	// };
	// const response = await fetchData(PUBLIC_SERVER + "/sessions/", requestInit);
	// if (!response.ok) return error(response.status, response.statusText);

	return goto("/login");
};

export const login = async (email: string) => {
	const requestInit: RequestInit = {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({ email })
	};

	const response = await fetch(PUBLIC_SERVER + "/sessions/", requestInit);

	if (!response.ok) return error(response.status, response.statusText);

	return response;
};

export const getRandomId = () => {
	const date = new Date();
	const timestamp = date.getTime();
	const randomNumber = Math.floor(Math.random() * 0xf);
	return `${timestamp.toString(16)}-${randomNumber.toString(16)}`;
};

const clearSessionStorage = () => {
	account.set(null);
	sessionStorage.removeItem("account");
	sessionStorage.removeItem("token");
};
