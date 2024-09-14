import { PUBLIC_SERVER } from "$env/static/public";
import { fetchData } from "$lib/utils";

export const getUnreadNotifications = async (receiverId: number) => {
  const response = await fetchData(
    PUBLIC_SERVER + "/notifications/comments/receivers/" + receiverId + "?is_read=false"
  );

  const notifications = response.json();

  return notifications;
};

export const getAllNotifications = async (receiverId: number) => {
  const response = await fetchData(
    PUBLIC_SERVER + "/notifications/comments/receivers/" + receiverId
  );

  const notifications = response.json();

  return notifications;
};

export const readNotification = async (receiverId: number, notificationId: number) => {
  const requestInit: RequestInit = {
    method: "PATCH",
    body: JSON.stringify({ is_read: true })
  };

  const response = await fetchData(
    PUBLIC_SERVER + `/notifications/comments/receivers/${receiverId}/${notificationId}/`,
    requestInit
  );

  const notifications = response.json();

  return notifications;
};

export const dismissNotification = async (receiverId: number, notificationId: number) => {
  const requestInit: RequestInit = {
    method: "DELETE"
  };

  const response = await fetchData(
    PUBLIC_SERVER + `/notifications/comments/receivers/${receiverId}/${notificationId}/`,
    requestInit
  );

  return response;
};
