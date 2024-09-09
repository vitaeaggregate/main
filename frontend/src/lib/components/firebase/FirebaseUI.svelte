<script lang="ts">
	import { createOrGetAccount } from "$lib/api/account";
	import { firebaseAuth } from "$lib/configs/firebase";
	import type Account from "$lib/interfaces/member/Account";
	import { account, checkAccountAndRedirect } from "$lib/store";
	import {
		EmailAuthProvider,
		GoogleAuthProvider,
		signInWithEmailAndPassword,
		type User
	} from "firebase/auth";
	import type { auth } from "firebaseui";
	import { onDestroy, onMount } from "svelte";
	import InputText from "$lib/components/InputText.svelte";
	import { error } from "@sveltejs/kit";
	import Button from "$lib/components/Button.svelte";
	import { goto } from "$app/navigation";

	let firebaseui: any = null;
	let firebaseUi: auth.AuthUI | null = null;
	let firebaseUiContainer: HTMLDivElement | null = null;
	let email: string = "";
	let password: string = "";

	onMount(async () => {
		if (!firebaseUiContainer) return;

		firebaseui = await import("firebaseui");

		const googleAuthProvider = new GoogleAuthProvider();
		const emailAuthProvider = new EmailAuthProvider();

		firebaseUi = new firebaseui.auth.AuthUI(firebaseAuth);

		if (!firebaseUi) return;

		firebaseUi.start(firebaseUiContainer, {
			signInFlow: "popup",
			signInOptions: [googleAuthProvider.providerId, emailAuthProvider.providerId]
		});

		firebaseAuth.onAuthStateChanged(async (user) => {
			if (!user) return;
			saveUser(user);
		});
	});

	onDestroy(() => {
		if (firebaseUi) firebaseUi.delete();
	});

	const handleLoginClick = () => {
		signInWithEmailAndPassword(firebaseAuth, email, password)
			.then((userCredential) => {
				// Signed in
				const user = userCredential.user;
				// ...
				saveUser(user);
			})
			.catch((err) => {
				const errorCode = err.code;
				const errorMessage = err.message;
				throw error(err.code, err.message);
			});
	};

	const saveUser = async (user: User) => {
		const token = await user.getIdToken();
		const response: Account = await createOrGetAccount(token);
		account.set(response);
		sessionStorage.setItem("account", JSON.stringify(response));
		sessionStorage.setItem("token", token);
		if ($account) goto("/");
	};
</script>

<div class="flex justify-center">
	<div class="flex w-fit flex-col items-center gap-4">
		<h1>Login</h1>
		<form action="">
			<div class="flex flex-col gap-5">
				<InputText placeholder="Email" bind:value={email}></InputText>
				<InputText type="password" placeholder="Password" bind:value={password}></InputText>
				<Button on:click={handleLoginClick}>Login</Button>
			</div>
		</form>
		<div class="relative flex w-full items-center">
			<div class="flex-grow border-t border-gray-400"></div>
			<span class="mx-4 flex-shrink text-gray-400">Or</span>
			<div class="flex-grow border-t border-gray-400"></div>
		</div>
		<div bind:this={firebaseUiContainer} class="flex w-full items-center justify-center"></div>
	</div>
</div>

{#if firebaseUiContainer}
	<style>
		@import "firebaseui/dist/firebaseui.css";
	</style>
{/if}
