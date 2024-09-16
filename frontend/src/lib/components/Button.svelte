<script context="module" lang="ts">
  export type Style =
    | "default"
    | "submit"
    | "full-width"
    | "add"
    | "cancel"
    | "sections"
    | "delete"
    | "delete-md"
    | "labeled-icon";
</script>

<script lang="ts">
  export let style: Style = "default";
  let classes: string;

  switch (style) {
    case "default": {
      classes = "size-fit";
      break;
    }
    case "submit": {
      classes =
        "size-fit border-2 bg-white pl-3 pr-3 pt-1 pb-1 m-auto hover:bg-lime hover:text-white hover:ease-in duration-200 rounded-md";
      break;
    }
    case "full-width": {
      classes = "w-full";
      break;
    }
    case "add": {
      classes =
        "size-fit h-max w-max rounded-xl bg-amber-600 p-3 shadow-lg text-center bg-opacity-80";
      break;
    }
    case "cancel": {
      classes = "size-fit h-max w-max rounded-xl bg-red-700 p-3 shadow-lg text-center";
      break;
    }
    case "sections": {
      classes = "size-fit bg-white border-2 rounded-lg p-3 hover:bg-amber-600";
      break;
    }
    case "delete": {
      classes = "size-fit flex h-max w-max rounded-xl bg-amber-600 p-3 shadow-lg";
      break;
    }
    case "delete-md": {
      classes = "flex h-max rounded-xl bg-amber-600 p-3 shadow-lg justify-center w-20";
      break;
    }
    case "labeled-icon": {
      classes = "flex gap-3 h-max rounded-xl bg-white p-3 shadow-lg justify-center";
    }
  }
</script>

<button type="button" on:click class={classes}>
  <slot></slot>
</button>
