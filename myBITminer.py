from hashlib import sha256

MAX_nonce = 100000000000

def SHA256(block_data):
    return sha256(block_data.encode("ascii")).hexdigest()

def miner(transaction, previous_hash, prefix_zeros,merkle_t_root,timestamp):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_nonce):
        block_data = transaction + previous_hash + str(nonce) + merkle_t_root + timestamp
        new_hash = SHA256(block_data)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoin with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct HASH after trying {MAX_nonce} times")

if __name__=='__main__':

    # Initial block data (transaction,hash of the previous block,merkle tree root, timestamp)
    transaction="03ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f"
    previous_hash="f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000"
    merkle_t_root="636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a010000004"
    timestamp="te472edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab9q"

    #the no. of zeros defines the no. of zeros in starting of the hash to be found
    no_of_zeros=2
    #changing this to higher number will consume more time for mining as difficulty increases
    
    import time     #using a time function to show the time taken to mine
    start_time = time.time()
    print("BitCoin Mining Started. . . . . . . .\n")
    new_hash = miner(transaction,previous_hash, no_of_zeros,merkle_t_root,timestamp)
    total_time = str((time.time() - start_time))

    print("\nThe new HASH found is: ",new_hash)
    print(f"\nwhich took: {total_time} seconds\n")
