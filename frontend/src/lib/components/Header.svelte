<script lang="ts">
  import { onMount } from "svelte";
  import { getUnreadNotifications, readNotification } from "$lib/api/commentNotification";
  import BellIcon from "$lib/icons/bell-icon.svelte";
  import type CommentNotification from "$lib/interfaces/member/CommentNotification";
  import CommentNotificationView from "$lib/components/CommentNotificationView.svelte";
  import Button from "$lib/components/Button.svelte";
  import { goto } from "$app/navigation";
  import { account } from "$lib/store";
  import { logout } from "$lib/utils";

  let commentNotifications: CommentNotification[] = [];

  let isNotificationsViewHidden = true;
  let isDropdownOpen = false;

  onMount(() => {
    loadUnreadNotifications();
    setInterval(loadUnreadNotifications, 5000);
  });

  const loadUnreadNotifications = async () => {
    if (!$account) return;
    const results: CommentNotification[] = await getUnreadNotifications($account.id);
    if (results) commentNotifications = results;
  };

  const handleNotificationsView = () => {
    if (!$account) return;
    if (isNotificationsViewHidden) isNotificationsViewHidden = false;
    else {
      isNotificationsViewHidden = true;
      if (commentNotifications && commentNotifications.length) {
        commentNotifications.forEach(
          async (commentNotification) => await readNotification($account.id, commentNotification.id)
        );
      }
      commentNotifications = [];
    }
  };

  const handleDropdownClick = () => {
    isDropdownOpen = !isDropdownOpen;
  }

  const handleDropdownFocusLoss = ({ relatedTarget, currentTarget }) => {
    if (relatedTarget instanceof HTMLElement && currentTarget.contains(relatedTarget)) return 
    isDropdownOpen = false
  }

</script>

<header class="flex justify-center bg-slate-200 p-4 px-10">
  <div class="container">
    <div class="flex justify-between">
      {#if $account}
        <nav class="relative flex justify-start gap-10">
         <!--  <div class="flex items-center gap-3">
            <a href="/my/page">My Page </a>
            <Button on:click={handleNotificationsView}>
              <div class="relative size-6">
                <BellIcon></BellIcon>
                {#if commentNotifications.length}
                  <span
                    class="absolute -right-3 -top-2 rounded-full bg-slate-100 px-2 text-sm ring-1"
                  >
                    {commentNotifications.length}
                  </span>
                {/if}
              </div>
            </Button>
          </div>
          <a href="/community">Community</a>
          {#if !isNotificationsViewHidden}
            <div class="item absolute top-full rounded-lg border-2 bg-slate-50 p-5">
              <h3>
                <a on:click={handleNotificationsView} href="/my/notifications">Notifications</a>
              </h3>

              <div role="button" aria-hidden="true" on:click={handleNotificationsView}>
                <CommentNotificationView bind:value={commentNotifications} type="dropdown"
                ></CommentNotificationView>
              </div>
            </div>
          {/if} -->
        
        <div class="dropdown flex justify-start items-center" on:focusout={handleDropdownFocusLoss}>
          <button class="btn m-1 " on:click={handleDropdownClick} >
          {#if isDropdownOpen}
            <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      class="inline-block h-6 w-6 stroke-current">
                      <title>Close Dropdown</title>
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M6 18L18 6M6 6l12 12" />
                    </svg>
            {:else}
            <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      class="inline-block h-6 w-6 stroke-current">
                      <title>Open Dropdown</title>
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M4 6h16M4 12h16M4 18h16" />
                    </svg>
            {/if}
          </button>
          <ul class="dropdown-content menu p-2 shadow bg-slate-200 rounded-box w-52 leading-9 absolute top-14" style:visibility={isDropdownOpen ? 'visible' : 'hidden'}>
            <li><button class="btn text-black ml-2"><a href="/my/page">My Page </a></button></li>
            <li><button class="btn text-black ml-2"><a href="/community">Community</a></button></li>
          </ul>
        </div>
        <Button on:click={handleNotificationsView}>
          <div class="relative size-6 mt-1.5">
            <BellIcon></BellIcon>
            {#if commentNotifications.length}
              <span
                class="absolute -right-3 -top-2 rounded-full bg-slate-100 px-2 text-sm ring-1"
              >
                {commentNotifications.length}
              </span>
            {/if}
          </div>
        </Button>
        {#if !isNotificationsViewHidden}
            <div class="item absolute rounded-lg border-2 bg-slate-50 p-5 top-14">
              <h3>
                <a on:click={handleNotificationsView} href="/my/notifications">Notifications</a>
              </h3>

              <div role="button" aria-hidden="true" on:click={handleNotificationsView}>
                <CommentNotificationView bind:value={commentNotifications} type="dropdown"
                ></CommentNotificationView>
              </div>
            </div>
          {/if}
        </nav>
      {:else}
        <nav></nav>
      {/if}
      {#if !$account}
        <button on:click={() => goto("/login/test")}>Login</button>
      {:else}
        <button on:click={logout}>Logout</button>
      {/if}
    </div>
  </div>
</header>
