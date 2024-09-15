<script context="module" lang="ts">
  export interface Config {
    isHidden?: boolean;
  }
</script>

<script lang="ts">
  import Button from "$lib/components/Button.svelte";
    import CloseIcon from "$lib/icons/CloseIcon.svelte";
    import ReturnIcon from "$lib/icons/ReturnIcon.svelte";

  export let backClick: ((event: Event) => void) | null = null;
  export let closeClick: ((event: Event) => void) | null;
  // export let config: {
  //   closeText?: string;
  // } = {
  //   closeText: "Close"
  // };

  let modal: HTMLDivElement | null = null;
</script>

<div bind:this={modal} class="fixed left-0 top-0 z-50 flex size-full items-center justify-center">
  <div
    role="button"
    on:keyup={closeClick}
    tabindex={0}
    class="absolute -z-10 size-full bg-slate-100 bg-opacity-65"
    on:click={closeClick}
  ></div>
  <div class="m-5 rounded-lg shadow-lg border-2 bg-white p-6 leading-9 max-h-128 overflow-y-auto w-80">
    <div class="flex justify-end gap-5 -mt-3">
      {#if backClick}
       <div class="mt-1.5"><Button on:click={backClick}><ReturnIcon /></Button></div>
      {/if}
      <Button on:click={closeClick}><CloseIcon /></Button>
    </div>
    <slot></slot>
  </div>
</div>
