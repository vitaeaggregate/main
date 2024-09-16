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
  import Logo from "$lib/Logo.png"

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
  };

  const handleDropdownFocusLoss = ({ relatedTarget, currentTarget }) => {
    if (relatedTarget instanceof HTMLElement && currentTarget.contains(relatedTarget)) return;
    isDropdownOpen = false;
  };
  const handleNotificationFocusLoss = ({ relatedTarget, currentTarget }) => {
    if (relatedTarget instanceof HTMLElement && currentTarget.contains(relatedTarget)) return;
    isNotificationsViewHidden = true;
  };
</script>

<header class="flex justify-center bg-green p-4 px-10">
  <div class="container ">
    <div class="flex justify-between">
      {#if $account}
        <nav class="flex items-center gap-3">
          <div
            class="dropdown flex items-center justify-start"
            on:focusout={handleDropdownFocusLoss}
          >
            <button class="btn m-1 -ml-3" on:click={handleDropdownClick}>
              {#if isDropdownOpen}
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  class="inline-block h-6 w-6 stroke-current"
                >
                  <title>Close Dropdown</title>
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M6 18L18 6M6 6l12 12"
                  />
                </svg>
              {:else}
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  class="inline-block h-6 w-6 stroke-current"
                >
                  <title>Open Dropdown</title>
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                </svg>
              {/if}
            </button>
            <ul
              class="dropdown-content menu rounded-box absolute top-20 w-52 bg-white p-2 leading-9 shadow-xl -ml-3"
              style:visibility={isDropdownOpen ? "visible" : "hidden"}
            >
              <li><button class="btn ml-2 text-black"><a href="/my/page">My Page </a></button></li>
              <li>
                <button class="btn ml-2 text-black"><a href="/community">Community</a></button>
              </li>
            </ul>
          </div>
          <div class="dropdown flex items-center justify-center rounded-full p-2 place-content-center shadow-lg bg-orange hover:bg-lime"
          on:focusout={handleNotificationFocusLoss}>
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
            {#if !isNotificationsViewHidden}
              <div class="item absolute top-20 left-5 rounded-lg border-2 bg-white p-5 shadow-lg">
                <h3 class="">
                  Notifications
                </h3>
                <a on:click={handleNotificationsView} href="/my/notifications" class="italic">See all</a>
                <br /><br />
                <div role="button" aria-hidden="true" on:click={handleNotificationsView}>
                  <CommentNotificationView bind:value={commentNotifications} type="dropdown"
                  ></CommentNotificationView>
                </div>
              </div>
            {/if}
          </div>
        </nav>
      {:else}
        <nav></nav>
      {/if}
      <img src={Logo} alt="Logo" class="h-10 w-auto" />
      {#if !$account}
        <button on:click={() => goto("/login/test")} class="-mr-3">Login</button>
      {:else}
        <button on:click={logout} class="-mr-3">Logout</button>
      {/if}
    </div>
  </div>
</header>
