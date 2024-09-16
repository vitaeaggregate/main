<script>
  import "../app.css";
  import TimeAgo from "javascript-time-ago";
  import { onMount } from "svelte";
  import en from "javascript-time-ago/locale/en";
  import { getSessionStorage } from "$lib/utils";

  onMount(() => {
    getSessionStorage();
    TimeAgo.addDefaultLocale(en);
  });
</script>

<div class="z-10 flex w-full grow flex-col gap-5 bg-orange">
  <slot></slot>
</div>
