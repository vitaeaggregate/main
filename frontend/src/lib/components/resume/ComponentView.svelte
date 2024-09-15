<script context="module" lang="ts">
  export interface ComponentConfig {
    readOnly?: boolean;
    isList?: boolean;
    unitLabel: string;
  }
</script>

<script lang="ts">
  import Button from "$lib/components/Button.svelte";
  import Modal from "$lib/components/Modal.svelte";
  import EditModal from "$lib/components/resume/EditModal.svelte";
  import { type BaseResumeTypes } from "$lib/interfaces/resume/BaseResumeTypes";
  import { type ComponentType } from "svelte";
  import SectionCard from "./SectionCard.svelte";

  import { slide } from "svelte/transition";

  export let value: BaseResumeTypes;
  export let component: ComponentType | null = null;
  export let config: ComponentConfig = {
    unitLabel: "",
    readOnly: false,
    isList: false
  };

  let isVisible = false;
  let currentSection: BaseResumeTypes<true> | null;

  const handleRemove = (id: string | number) => {
    if (Array.isArray(value)) value = [...value.filter((value) => value.id !== id)];
  };

  const handleEdit = (section: BaseResumeTypes<true>) => {
    currentSection = section;
  };

  const closeModalClick = () => {
    currentSection = null;
  };

  $: {
    if (Array.isArray(value))
      value = value.map((section) => {
        if (currentSection && currentSection.id == section.id) return section;
        else return section;
      });
  }
</script>

{#if component && currentSection}
  <Modal closeClick={closeModalClick}>
    <EditModal
      {component}
      bind:value={currentSection}
      {closeModalClick}
      title={`Edit ${config.unitLabel}`}
    ></EditModal>
  </Modal>
{/if}
{#if Array.isArray(value) && value.length}
  <SectionCard>
    <Button on:click={() => (isVisible = isVisible ? false : true)} style="full-width">
      <h2>
        {config.unitLabel + "s"}
      </h2>
    </Button>
    {#if isVisible}
      <div
        class="flex flex-col divide-y"
        in:slide={{ axis: "y", duration: 800 }}
        out:slide={{ axis: "y", duration: 800 }}
      >
        {#each value as item (item.id)}
          <div class="flex flex-col gap-3 p-2">
            <svelte:component
              this={component}
              bind:value={item}
              readOnly={config.readOnly}
              isList={config.isList}
            ></svelte:component>
            <div class="flex gap-10">
              <Button on:click={() => handleEdit(item)}>Edit</Button>
              <Button on:click={() => item.id && handleRemove(item.id)}>Remove</Button>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </SectionCard>
{:else if !Array.isArray(value)}
  <div class="flex flex-col">
    <h2>{config.unitLabel}</h2>
    <svelte:component this={component} bind:value readOnly={config.readOnly}></svelte:component>
  </div>
{/if}
