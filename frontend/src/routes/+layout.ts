import { initializeFirebase, auth } from "$lib/firebase/firebase.client";
import { browser } from "$app/environment";
import { onAuthStateChanged } from "firebase/auth";

// Firebase functions
export async function load({ url }) {
	if (browser) {
		try {
			initializeFirebase();
		} catch (error) {
			console.log(error);
		}
	}

	function getAuthUser() {
		return new Promise((resolve) => {
			onAuthStateChanged(auth, (user) => resolve(user ? user : false));
		});
	}
	return {
		getAuthUser: getAuthUser,
		url: url.pathname
	};
}
