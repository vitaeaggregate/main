<script lang="ts">
  import Button from "$lib/components/Button.svelte";
  import type { BaseResumeTypes } from "$lib/interfaces/resume/BaseResumeTypes";
  import { onMount, tick, type ComponentType } from "svelte";

  export let component: ComponentType;
  export let value: BaseResumeTypes<true> = {};
  export let title: string = "";
  export let closeModalClick: () => void;

  let initialValue: BaseResumeTypes<true> = {};

  onMount(() => (initialValue = { ...value }));

  const handleCancelClick = () => {
    if (!value) return;
    for (const key in initialValue) value[key] = initialValue[key];
    closeModalClick();
  };
</script>

<div class="flex flex-col gap-3">
  <h2>{title}</h2>
  <svelte:component this={component} bind:value></svelte:component>
  <div class="flex justify-between px-5">
    <Button on:click={closeModalClick} style="add">Save</Button>
    <Button on:click={handleCancelClick} style="cancel">Cancel</Button>
  </div>
</div>
