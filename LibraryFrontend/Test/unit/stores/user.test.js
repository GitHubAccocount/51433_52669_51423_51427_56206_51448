import { setActivePinia, createPinia } from "pinia";
import { beforeEach, describe, it, expect, vi } from "vitest";
import axios from "axios";
import { createTestingPinia } from "@pinia/testing";
import { useUserStore } from "@/stores/user";

vi.mock("axios");
vi.mock("vue-router", () => ({
  useRouter: () => ({
    push: vi.fn(),
  }),
}));

describe("useUserStore", () => {
  beforeEach(() => {
    setActivePinia(createPinia());
  });

  it("should have initial state", () => {
    const store = useUserStore();
    expect(store.errors).toEqual([]);
    expect(store.isSubmitting).toBe(false);
    expect(store.user).toEqual({
      isAuthenticated: false,
      id: null,
      email: null,
      access: null,
      refresh: null,
    });
  });

  it("should log in successfully", async () => {
    const store = useUserStore();
    const mockResponseData = {
      access: "mock_access_token",
      refresh: "mock_refresh_token",
    };

    axios.post.mockResolvedValue({ data: mockResponseData });
    axios.get.mockResolvedValue({ data: { email: "test@example.com", id: 1 } });

    const form = { email: "test@example.com", password: "password" };
    await store.LOGIN(form);

    expect(store.user.isAuthenticated).toBe(true);
    expect(store.user.access).toBe("mock_access_token");
    expect(store.user.email).toBe("test@example.com");
    expect(store.user.id).toBe(1);
  });

  it("should handle login errors", async () => {
    const store = useUserStore();
    const mockError = { response: { data: { detail: "Invalid credentials" } } };
    axios.post.mockRejectedValue(mockError);

    const form = { email: "test@example.com", password: "wrong_password" };
    await store.LOGIN(form);

    expect(store.errors).toEqual(["Invalid credentials"]);
  });

  it("should log out successfully", () => {
    const store = useUserStore();
    localStorage.setItem("user.access", "mock_access_token");

    store.LOGOUT();
    expect(store.user.isAuthenticated).toBe(false);
    expect(localStorage.getItem("user.access")).toBeNull();
  });
});
