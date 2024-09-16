<script lang="ts">
  import Button from "$lib/components/Button.svelte";
  import type { BaseResumeTypes } from "$lib/interfaces/resume/BaseResumeTypes";
  import { onMount, tick, type ComponentType } from "svelte";

  export let component: ComponentType;
  export let value: BaseResumeTypes<true> = {};
  export let title: string = "";
  export let closeModalClick: () => void;

  let initialValue: BaseResumeTypes<true> = {};

  onMount(() => {
    initialValue = { ...value };
  });

  const handleCancelClick = () => {
    if (!value) return;
    for (const key in initialValue) value[key] = initialValue[key];
    closeModalClick();
  };
</script>

<div>
  <h2>{title}</h2>
  <svelte:component this={component} bind:value></svelte:component>
  <Button on:click={closeModalClick}>Save</Button>
  <Button on:click={handleCancelClick}>Cancel</Button>
</div>
