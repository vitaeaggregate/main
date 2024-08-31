import { env } from "$env/dynamic/public";

export async function createOrGetAccount(token: string) {
	const endPoint = "firebase/accounts/";
	const fetchConfig: RequestInit = {
		method: "POST",
		headers: {
			"Content-Type": "applications/json",
			Authorization: `Bearer ${token}`
		}
	};

	const response = await fetch(env.PUBLIC_SERVER + endPoint, fetchConfig);

	if (response.ok) console.log("Token sent successfully");
	else console.error("Failed to send token");
}
