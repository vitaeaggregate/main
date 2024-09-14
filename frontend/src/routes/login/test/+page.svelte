<script lang="ts">
  import { goto } from "$app/navigation";
  import type Account from "$lib/interfaces/member/Account";
  import InputText from "$lib/components/InputText.svelte";
  import { login } from "$lib/utils";
  import { account } from "$lib/store";

  interface ServerResponse {
    account: Account;
    token: string;
  }

  let email = "";

  $: if ($account) goto("/community", { replaceState: true });

  let handleSubmit = async () => {
    const response = await login(email);

    const json: ServerResponse = await response.json();

    account.set(json.account);
    sessionStorage.setItem("account", JSON.stringify(json.account));
    sessionStorage.setItem("token", json.token);

    // goto("/my/page");
  };
</script>

{#if $account === null}
  <section class="flex w-full justify-center p-10">
    <form class="flex max-w-52 flex-col items-center gap-5">
      <h2>Login</h2>
      <InputText bind:value={email} placeholder="Email" />
      <button on:click={handleSubmit}>Enter</button>
    </form>
  </section>
{/if}
