def validUTF8(data):
        # Number of bytes in the current UTF-8 character
            n_bytes = 0

                # For each integer in the data array
                    for num in data:
                                # Get the binary representation. We only need the least significant 8 bits
                                        # for any given number, so we discard the rest.
                                                bin_rep = format(num, '#010b')[-8:]

                                                        # If this is the case then we are to start processing a new UTF-8 character.
                                                                if n_bytes == 0:
                                                                                # Get the number of 1s in the beginning of the string.
                                                                                            if bin_rep[0] == '0': n_bytes = 0
                                                                                                        elif bin_rep[0:3] == '110': n_bytes = 1
                                                                                                                    elif bin_rep[0:4] == '1110': n_bytes = 2
                                                                                                                                elif bin_rep[0:5] == '11110': n_bytes = 3
                                                                                                                                            else: return False

                                                                                                                                                    # Else, we are to account for the remaining bytes if any.
                                                                                                                                                            else:
                                                                                                                                                                            # Else, only the least significant 2 bits matter (the 6 rest are to
                                                                                                                                                                                        # ensure correct formating).
                                                                                                                                                                                                    if bin_rep[0:2] == '10':
                                                                                                                                                                                                                        n_bytes -= 1
                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                        return False

                                                                                                                                                                                                                                                        # This is for the case where we might not have the complete data for
                                                                                                                                                                                                                                                            # a particular UTF-8 character.
                                                                                                                                                                                                                                                                return n_bytes == 0
