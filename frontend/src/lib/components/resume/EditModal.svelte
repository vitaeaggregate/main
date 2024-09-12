<script lang="ts">
  import Button from "$lib/components/Button.svelte";
  import { onMount, tick, type ComponentType } from "svelte";

  export let component: ComponentType;
  export let value: {};
  export let title: string = "";
  export let closeModalClick: () => void;

  let initialValue: {};

  onMount(() => {
    initialValue = { ...value };
  });

  const handleCancelClick = () => {
    value = { ...initialValue };
    closeModalClick();
  };
</script>

<div>
  <h2>{title}</h2>
  <svelte:component this={component} bind:value></svelte:component>
  <Button on:click={closeModalClick}>Save</Button>
  <Button on:click={handleCancelClick}>Cancel</Button>
</div>
