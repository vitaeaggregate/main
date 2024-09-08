import { initializeApp } from "firebase/app";
import { connectAuthEmulator, getAuth, setPersistence, inMemoryPersistence } from "firebase/auth";
import type { FirebaseApp } from "firebase/app";
import type { Firestore } from "firebase/firestore";
import type { Auth } from "firebase/auth";
import { browser } from "$app/environment";
import {
	PUBLIC_API_KEY,
	PUBLIC_APP_ID,
	PUBLIC_AUTH_DOMAIN,
	PUBLIC_SERVER,
	PUBLIC_SERVER_FIREBASE,
	PUBLIC_USE_EMULATOR
} from "$env/static/public";

import firebase from "firebase/compat/app";

export let dv: Firestore;
export let app: FirebaseApp;
export let auth: Auth;

const firebaseConfig = {
	apiKey: PUBLIC_API_KEY,
	appId: PUBLIC_APP_ID,
	useEmulator: PUBLIC_USE_EMULATOR === "true",
	authDomain: PUBLIC_AUTH_DOMAIN
};

export const initializeFirebase = () => {
	if (!browser) {
		throw new Error("Can't use Firebase client on the server.");
	}
	if (!app) {
		app = initializeApp(firebaseConfig);
		auth = getAuth(app);
		console.log("we're here");
		console.log(app);

		if (firebaseConfig.useEmulator) {
			connectAuthEmulator(auth, PUBLIC_SERVER);
		}
	}
};
