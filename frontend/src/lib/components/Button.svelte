<script context="module" lang="ts">
  export type Style = "default" | "submit" | "add" | "cancel" | "sections" | "delete";
</script>

<script lang="ts">
  export let style: Style = "default";
  let classes: string = "size-fit ";

  switch (style) {
    case "default": {
      break;
    }
    case "submit": {
      classes +=
        "border-2 bg-white pl-3 pr-3 pt-1 pb-1 m-auto hover:bg-lime hover:text-white hover:ease-in duration-200 rounded-md";
      break;
    }
    case "add": {
      classes +=
      "h-max w-max rounded-xl bg-amber-600 p-3 shadow-lg text-center";
      break;
    }
    case "cancel": {
      classes +=
      "h-max w-max rounded-xl bg-red-700 p-3 shadow-lg text-center";
      break;
    }
    case "sections": {
      classes +=
      "bg-white border-2 rounded-lg p-3 hover:bg-amber-600";
      break;
    }
    case "delete": {
      classes +=
      "flex h-max w-max rounded-xl bg-amber-600 p-3 shadow-lg";
      break;
    }
  }
</script>

<button type="button" on:click class={classes}>
  <slot></slot>
</button>
