<script lang="ts">
  import { goto } from "$app/navigation";
	import CommunityIcon from "$lib/icons/CommunityIcon.svelte";
	import HomeIcon from "$lib/icons/HomeIcon.svelte";
	import LogoutIcon from "$lib/icons/LogoutIcon.svelte";
  import { account } from "$lib/store";
  import { logout } from "$lib/utils";

</script>

<footer class="fixed bottom-0 h-16 left-0 w-full py-5 text-center flex justify-center bg-white p-5 px-10 border-solid border-1 border-gray-400 rounded drop-shadow-lg outline-none">
    <div class="container">
        <div class="flex justify-between">
          {#if $account}
          <nav class="grid grid-cols-2 gap-10">
            <div class="flex items-center flex-nowrap">
              <HomeIcon />
              <a href="/my/page">My Page</a>
            </div>
            <div class="flex items-center flex-nowrap">
                <CommunityIcon />
            <a href="/community">Community</a></div>
          </nav>
          {:else}
            <nav></nav>
          {/if}
          {#if !$account}
          <div class="flex items-center flex-nowrap">
            <LogoutIcon />
            <button on:click={() => goto("/login/test")}>Login</button></div>
          {:else}
            <button on:click={logout}>Logout</button>
          {/if}
        </div>
      </div>
  </footer>