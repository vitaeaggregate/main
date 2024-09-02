import { goto } from "$app/navigation";
import { PUBLIC_SERVER } from "$env/static/public";
import { error } from "@sveltejs/kit";
import { account } from "./store";

export const fetchData = async (url: string, requestInit: RequestInit) => {
	if (!sessionStorage.getItem("token")) return error(400, "No token");

	const token = sessionStorage.getItem("token") || "";

	if (token === "") {
		return error(400, "No token");
	}

	requestInit.headers = requestInit.headers
		? {
				...requestInit.headers,
				"Content-Type": "application/JSON",
				Authorization: token
			}
		: {
				"Content-Type": "application/JSON",
				Authorization: token
			};

	const response = await fetch(url, requestInit);

	if (!response.ok) {
		if (response.status === 401) logout();
		return error(response.status, response.statusText);
	}

	return response;
};

export const logout = async () => {
	const requestInit: RequestInit = {
		method: "DELETE"
	};

	const response = await fetchData(PUBLIC_SERVER + "/sessions/", requestInit);

	if (!response.ok) return error(response.status, response.statusText);

	clearSessionStorage();

	return goto("/");
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

const clearSessionStorage = () => {
	account.set(null);
	sessionStorage.removeItem("account");
	sessionStorage.removeItem("token");
};
