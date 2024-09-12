import { writable } from "svelte/store";
import type Account from "$lib/interfaces/member/Account";
import { goto } from "$app/navigation";
import type CommentNotification from "./interfaces/member/CommentNotification";

export const account = writable<Account | null>();

export const commentNotifications = writable<CommentNotification[] | null>();

export const checkAccountAndRedirect = (callBack?: () => void) => {
  account.subscribe(($account) => {
    if ($account && Object.keys($account).length && callBack) callBack();
    else if ($account === null || ($account && !Object.keys($account).length))
      goto("/login", { replaceState: false });
  });
};

export const toasts = writable([]);

export const addToast = (toast) => {
  const id = Math.floor(Math.random() * 10000);
  console.log(toast);

  const defaults = {
    id,
    type: "info",
    dismissible: true,
    timeout: 3000
  };

  toasts.update((all) => [{ ...defaults, ...toast }, ...all]);

  if (toast.timeout) setTimeout(() => dismissToast(id), toast.timeout);
};

export const dismissToast = (id: number) => {
  toasts.update((all) => all.filter((t) => t.id !== id));
};
