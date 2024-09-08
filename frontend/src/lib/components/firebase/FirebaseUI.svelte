<script lang="ts">
	import { createOrGetAccount } from "$lib/api/account";
	import { firebaseAuth } from "$lib/configs/firebase";
	import { EmailAuthProvider, GoogleAuthProvider } from "firebase/auth";
	import type { auth } from "firebaseui";
	import { onDestroy, onMount } from "svelte";

	let firebaseui: any = null;
	let firebaseUi: auth.AuthUI | null = null;
	let firebaseUiContainer: HTMLDivElement | null = null;

	onMount(async () => {
		if (!firebaseUiContainer) return;

		firebaseui = await import("firebaseui");

		const googleAuthProvider = new GoogleAuthProvider();
		const emailAuthProvider = new EmailAuthProvider();

		firebaseUi = new firebaseui.auth.AuthUI(firebaseAuth);

		if (!firebaseUi) return;

		firebaseUi.start(firebaseUiContainer, {
			signInOptions: [googleAuthProvider.providerId, emailAuthProvider.providerId],
			signInSuccessUrl: "/"
		});

		firebaseAuth.onAuthStateChanged(async (user) => {
			if (!user) return;

			console.log(user);
			
			const token = await user.getIdToken();
			const account = await createOrGetAccount(token);
		
			console.log(account)
		});
	});

	onDestroy(() => {
		if (firebaseUi) firebaseUi.delete();
	});
</script>

<div bind:this={firebaseUiContainer} class="flex w-full items-center justify-center"></div>

{#if firebaseUiContainer}
	<style>
		@import "firebaseui/dist/firebaseui.css";
	</style>
{/if}
