<script lang="ts">
  import { createOrGetAccount } from "$lib/api/account";
  import { firebaseAuth } from "$lib/configs/firebase";
  import type Account from "$lib/interfaces/member/Account";
  import { account } from "$lib/store";
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
  import Logo from "$lib/Logo.png";
  import Toasts from "../Toasts.svelte";
  import { addToast } from "$lib/store";

  let firebaseui: any = null;
  let firebaseUi: auth.AuthUI | null = null;
  let firebaseUiContainer: HTMLDivElement | null = null;
  let email: string = "";
  let password: string = "";

  let message = "";
  let type = "error";
  let dismissible = true;
  let timeout = 5000;

  onMount(async () => {
    if (!firebaseUiContainer) return;

    firebaseui = await import("firebaseui");

    const googleAuthProvider = new GoogleAuthProvider();
    const emailAuthProvider = new EmailAuthProvider();

    firebaseUi = new firebaseui.auth.AuthUI(firebaseAuth);

    if (!firebaseUi) return;

    firebaseUi.start(firebaseUiContainer, {
      signInFlow: "popup",
      signInSuccessUrl: "/my/page",
      signInOptions: [
        googleAuthProvider.providerId,
        { provider: emailAuthProvider.providerId, fullLabel: "Sign up with email" }
      ]
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
        message = "Please enter a valid username or password!";
        addToast({
          message,
          type,
          dismissible,
          timeout
        });
        throw error(err.code, err.message);
      });
  };

  const saveUser = async (user: User) => {
    const token = await user.getIdToken();
    const response: Account = await createOrGetAccount(token);
    account.set(response);
    sessionStorage.setItem("account", JSON.stringify(response));
    sessionStorage.setItem("token", token);
    goto("/my/page");
  };

  const handleSmoothScroll = (event) => {
    event.preventDefault();
    const link = event.currentTarget;
    const anchorId = new URL(link.href).hash.replace("#", "");
    const anchor = document.getElementById(anchorId);   

    if (anchor) {
      window.scrollTo({
        top: anchor.offsetTop,
        behavior: "smooth"   

      });
    }
  };
</script>

<div class="relative flex h-full justify-center">
  <Toasts />
  <div class="z-50 mt-8 flex w-fit flex-col items-center gap-4">
    <img src={Logo} alt="Logo" class="h-24 w-auto opacity-30" />
    <h1>Vitae Aggregate</h1>
    <h2>Welcome!</h2>
    <p class="text-4xl text-center">Mobile first<br />
      Never forget
      </p>
    <a href="#anchor-login" on:click={handleSmoothScroll}>Sign up or login</a>
    <h2 id="anchor-login">Login</h2>
    <form action="">
      <div class="flex flex-col gap-5">
        <InputText placeholder="Email" bind:value={email}></InputText>
        <InputText type="password" placeholder="Password" bind:value={password}></InputText>
        <Button on:click={handleLoginClick} style="submit">Login</Button>
      </div>
    </form>
    <div class="relative flex w-full items-center p-4">
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