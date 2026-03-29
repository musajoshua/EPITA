export function shorten(str: string, left = 25, right = 25) {
  if (str.length <= left + right + 3) return str;
  return `${str.slice(0, left)}...${str.slice(-right)}`;
}